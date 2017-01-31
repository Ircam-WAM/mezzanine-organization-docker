# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-06 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0035_auto_20170106_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'project call',
                'ordering': ['name'],
                'verbose_name_plural': 'project calls',
            },
        ),
        migrations.AlterField(
            model_name='project',
            name='referring_person',
            field=models.ManyToManyField(blank=True, related_name='projects_referring_person', to='organization-network.Person', verbose_name='Referring Person'),
        ),
        migrations.AddField(
            model_name='project',
            name='call',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='organization-projects.ProjectCall', verbose_name='project call'),
        ),
    ]