# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='starturl',
            field=models.CharField(default='/contacts', max_length=200),
        ),
    ]
