# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageentity',
            name='modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
