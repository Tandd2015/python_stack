# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-21 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0002_auto_20191021_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='total_order',
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='poorly_coded_store.User'),
        ),
    ]
