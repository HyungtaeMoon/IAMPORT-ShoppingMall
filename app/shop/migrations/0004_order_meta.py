# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 09:30
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181030_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='meta',
            field=jsonfield.fields.JSONField(blank=True, default={}),
        ),
    ]