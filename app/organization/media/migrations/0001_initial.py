# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('_meta_title', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('description_fr', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('content_fr', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_en', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('media_id', models.CharField(max_length=128, verbose_name='media id')),
                ('open_source_url', models.URLField(blank=True, max_length=1024, verbose_name='open source URL')),
                ('closed_source_url', models.URLField(blank=True, max_length=1024, verbose_name='closed source URL')),
                ('poster_url', models.URLField(blank=True, max_length=1024, verbose_name='poster')),
                ('site', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'audio',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('audios', models.ManyToManyField(blank=True, related_name='playlists', to='organization media.Audio', verbose_name='audios')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('_meta_title', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('description_fr', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('content_fr', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_en', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('media_id', models.CharField(max_length=128, verbose_name='media id')),
                ('open_source_url', models.URLField(blank=True, max_length=1024, verbose_name='open source URL')),
                ('closed_source_url', models.URLField(blank=True, max_length=1024, verbose_name='closed source URL')),
                ('poster_url', models.URLField(blank=True, max_length=1024, verbose_name='poster')),
            ],
            options={
                'verbose_name': 'video',
            },
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('site', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'video category',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='organization media.VideoCategory', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='video',
            name='site',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]
