# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20171009_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
