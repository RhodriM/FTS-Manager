# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20171006_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='send_notifications',
            field=models.BooleanField(default=True),
        ),
    ]
