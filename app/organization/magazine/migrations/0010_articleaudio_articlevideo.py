# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-05 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-media', '0003_auto_20160929_1835'),
        ('organization-magazine', '0009_auto_20160928_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleAudio',
            fields=[
                ('audio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organization-media.Audio')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audios', to='organization-magazine.Article', verbose_name='article')),
            ],
            options={
                'abstract': False,
            },
            bases=('organization-media.audio',),
        ),
        migrations.CreateModel(
            name='ArticleVideo',
            fields=[
                ('video_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organization-media.Video')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='organization-magazine.Article', verbose_name='article')),
            ],
            options={
                'abstract': False,
            },
            bases=('organization-media.video',),
        ),
    ]
