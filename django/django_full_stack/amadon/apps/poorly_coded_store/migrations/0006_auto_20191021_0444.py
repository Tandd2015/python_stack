# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-21 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0005_auto_20191021_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
