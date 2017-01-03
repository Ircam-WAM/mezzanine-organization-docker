# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-03 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0035_projectblock_login_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectblock',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='projectblock',
            name='content_fr',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='projectblock',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='projectblock',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='projectblock',
            name='title_en',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='projectblock',
            name='title_fr',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
    ]
