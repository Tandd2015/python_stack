# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-23 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list_app', '0002_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='items_list_object',
        ),
        migrations.AddField(
            model_name='item',
            name='items_list_object',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_list_object', to='wish_list_app.User'),
        ),
    ]
