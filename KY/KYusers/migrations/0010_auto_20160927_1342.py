# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-27 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYusers', '0009_auto_20160927_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caprofile',
            name='pincode',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
