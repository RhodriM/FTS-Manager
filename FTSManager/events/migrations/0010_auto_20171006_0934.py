# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 09:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentnotification',
            name='notification',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='events.Notification'),
            preserve_default=False,
        ),
    ]
