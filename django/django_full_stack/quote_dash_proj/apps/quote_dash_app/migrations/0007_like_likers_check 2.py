# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-22 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote_dash_app', '0006_auto_20191022_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='likers_check',
            field=models.BooleanField(default=False),
        ),
    ]
