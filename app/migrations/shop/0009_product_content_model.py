# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-25 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20160907_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_model',
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
    ]
