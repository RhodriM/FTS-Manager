# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_sentnotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('notice', models.DurationField()),
                ('speakers_only', models.BooleanField(default=True)),
                ('message', models.TextField()),
            ],
        ),
    ]