# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20160427_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=80),
        ),
    ]
