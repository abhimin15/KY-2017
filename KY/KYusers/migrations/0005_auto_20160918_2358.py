# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-18 18:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYusers', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='caprofile',
            name='fblink',
            field=models.CharField(default='sdlfkj', max_length=300, validators=[django.core.validators.URLValidator()]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caprofile',
            name='whyChooseYou',
            field=models.TextField(default='asdlkjf'),
            preserve_default=False,
        ),
    ]
