# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='presenter',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
