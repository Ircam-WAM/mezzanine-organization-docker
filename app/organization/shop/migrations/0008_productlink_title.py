# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-21 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-shop', '0007_auto_20161020_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlink',
            name='title',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='title'),
        ),
    ]
