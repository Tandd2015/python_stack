# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-18 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_maker', '0005_auto_20191018_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='rel_date',
            field=models.DateTimeField(default='2019/10/18 10:26 PM'),
        ),
    ]
