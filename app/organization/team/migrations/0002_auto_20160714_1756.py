# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='weaving_class',
        ),
        migrations.AddField(
            model_name='department',
            name='weaving_css_class',
            field=models.CharField(blank=True, max_length=64, verbose_name='weaving CSS class'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.TextField(blank=True, verbose_name='address'),
        ),
    ]
