# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_date', models.DateField()),
                ('news_text', models.CharField(max_length=50)),
            ],
        ),
    ]
