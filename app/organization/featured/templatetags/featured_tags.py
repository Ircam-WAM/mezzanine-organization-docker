# -*- coding: utf-8 -*-
from mezzanine.pages.models import Page
#from mezzanine.blog.models import BlogPost
from mezzanine.template import Library
from mezzanine_agenda.models import Event
from mezzanine.conf import settings
from random import shuffle

from organization.festival.models import *
from organization.featured.models import *

register = Library()


@register.filter
def subtract(value, arg):
    return value - arg

@register.as_tag
def featured_edito(*args):
    qs = Page.objects.filter(slug="edito")
    if qs:
        return qs[0].get_content_model()
    else:
        return None

@register.as_tag
def featured_events(*args):
    featured = Featured.objects.all()
    if featured:
        return featured[0].events.order_by('start')
    return None

@register.as_tag
def featured(*args):
    featured_list = []
    featured = Featured.objects.filter(id=settings.HOME_FEATURED_ID)
    if featured:
        featured = featured[0]
        for page in featured.pages.all():
            featured_list.append(page)
        for article in featured.articles.all():
            featured_list.append(article)
        for brief in featured.briefs.all():
            featured_list.append(brief)
        for video in featured.videos.all():
            featured_list.append(video)
        for playlist in featured.playlists.all():
            featured_list.append(playlist)
        shuffle(featured_list)
    return featured_list

@register.as_tag
def featured_breaking_news_content(*args):
    featured = Featured.objects.filter(id=settings.BREAKING_NEWS_FEATURED_ID)
    if featured:
        featured = featured[0]
        news = featured.pages.all()
        if news:
            return news[0].richtextpage.content
        else:
            return ''
    return ''

@register.filter
def get_class(obj):
    return obj.__class__.__name__

@register.filter
def unique_posts(events):
    post_list = []
    for event in events:
        for post in event.blog_posts.all():
            print(post)
            if not post in post_list:
                post_list.append(post)
    return post_list

@register.filter
def no_parents(events):
    return events.filter(parent=None)
