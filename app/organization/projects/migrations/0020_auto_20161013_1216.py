# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-13 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0019_auto_20161007_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectaudio',
            options={'verbose_name': 'Audio', 'verbose_name_plural': 'Audios'},
        ),
        migrations.AlterModelOptions(
            name='projectvideo',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
    ]
