# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-04 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0029_auto_20161004_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='organization-network.Team', verbose_name='parent team'),
        ),
    ]
