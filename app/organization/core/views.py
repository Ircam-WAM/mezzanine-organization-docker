from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic.base import View
from django.views.generic import DetailView, ListView, TemplateView
from django.apps import apps
from django.utils.translation import ugettext_lazy as _
from django.http import QueryDict
from mezzanine.conf import settings
from mezzanine.utils.views import paginate
from organization.core.models import *
from functools import reduce
from operator import ior, iand
from organization.media.models import Playlist
from mezzanine_agenda.models import Event
from organization.pages.models import CustomPage
from organization.projects.models import Project

class SlugMixin(object):

    def get_object(self):
        objects = self.model.objects.all()
        return get_object_or_404(objects, slug=self.kwargs['slug'])


class CustomSearchView(TemplateView):

    template_name='search_results.html'

    def get(self, request, *args, **kwargs):
        """
        Display search results. Takes an optional "contenttype" GET parameter
        in the form "app-name.ModelName" to limit search results to a single model.
        """
        context = super(CustomSearchView, self).get_context_data(**kwargs)
        query = request.GET.get("q", "")
        page = request.GET.get("page", 1)
        per_page = settings.SEARCH_PER_PAGE
        max_paging_links = settings.MAX_PAGING_LINKS
        is_searching_all = False
        try:
            parts = request.GET.get("type", "").split(".", 1)
            search_model = apps.get_model(*parts)
            search_model.objects.search  # Attribute check
        except (ValueError, TypeError, LookupError, AttributeError):
            search_model = Displayable
            search_type = _("Everything")
            is_searching_all = True
        else:
            search_type = search_model._meta.verbose_name_plural.capitalize()

        # @Todo : rewrite SearchableManager
        results = search_model.objects.search(query, for_user=request.user)
        results_media_count = len(Playlist.objects.search(query, for_user=request.user))
        results_page_count = len(CustomPage.objects.search(query, for_user=request.user))
        results_event_count = len(Event.objects.search(query, for_user=request.user))
        results_project_count = len(Project.objects.search(query, for_user=request.user))

        # count objects
        filter_dict = dict()

        for result in results:
            classname = result.__class__.__name__
            app_label = result._meta.app_label
            full_classname = app_label+"."+classname
            verbose_name = result._meta.verbose_name
            # aggregate all Page types : CustomPage, TeamPage, Topic etc...
            if result._meta.get_parent_list() :
                parent_class = result._meta.get_parent_list()[0]
                if full_classname in settings.PAGES_MODELS:
                    classname = "CustomPage"
                    verbose_name = "Page"
                    app_label = "organization-pages"
            elif classname == "Playlist":
                verbose_name = "Media"
            if classname in filter_dict:
                filter_dict[classname]['count'] += 1
            else:
                filter_dict[classname] = {'count' : 1}
                filter_dict[classname].update({'verbose_name' : verbose_name})
                filter_dict[classname].update({'app_label' : app_label})

        # temporarily overriding filter_dict to get all filters manually
        filter_dict = {
            'CustomPage': {
                'count' : results_page_count,
                'verbose_name' : 'Page',
                'app_label' : 'organization-pages'
            },
            'Event': {
                'count' : results_event_count,
                'verbose_name' : 'Event',
                'app_label' : 'mezzanine_agenda'
            },
            'Playlist': {
                'count' : results_media_count,
                'verbose_name' : 'Media',
                'app_label' : 'organization-media'
            },
            'Project': {
                'count' : results_project_count,
                'verbose_name' : 'Project',
                'app_label' : 'organization-projects'
            },
        }

        # get url param
        current_query = QueryDict(mutable=True)
        current_query = request.GET.copy()

        # generate filter url
        for key, value in filter_dict.items():
            current_query['type'] = value['app_label']+'.'+ key
            filter_dict[key].update({'url' : request.path+"?"+current_query.urlencode(safe='/')})

        # pagination
        paginated = paginate(results, page, per_page, max_paging_links)

        # count all results
        all_results_count = results_media_count + results_page_count + results_event_count

        # context
        context = {"query": query, "results": paginated,
                   "search_type": search_type.__class__.__name__, "search_model": search_model.__name__,
                   "all_results_count" : all_results_count, 'is_searching_all': is_searching_all}

        # cancel filter url
        if request.GET.__contains__('type'):
            previous_query = QueryDict(mutable=True)
            previous_query = request.GET.copy()
            previous_query.pop('type')
            context['cancel_filter_url'] = '?'+previous_query.urlencode(safe='/')

        context['filter_dict'] = filter_dict
        # context.update(extra_context or {})
        return self.render_to_response(context)
