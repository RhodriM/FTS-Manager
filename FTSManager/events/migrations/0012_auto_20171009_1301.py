# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_send_notifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='title',
            new_name='subject',
        ),
    ]
