# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170524_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursename',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
