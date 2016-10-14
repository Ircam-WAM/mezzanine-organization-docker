# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-13 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-media', '0008_auto_20161013_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization-media.Playlist', verbose_name='playlist')),
            ],
            options={
                'verbose_name': 'playlist',
                'verbose_name_plural': 'playlists',
            },
        ),
        migrations.AlterModelOptions(
            name='mediatranscoded',
            options={'verbose_name': 'media file', 'verbose_name_plural': 'media files'},
        ),
    ]
