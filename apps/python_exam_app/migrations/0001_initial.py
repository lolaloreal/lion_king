# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-27 19:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=200)),
                ('plan', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name=datetime.date.today)),
                ('end_date', models.DateTimeField(verbose_name=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]