# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-09 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYusers', '0020_college_regcount'),
        ('events', '0004_auto_20161110_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contingent',
            name='members',
        ),
        migrations.AddField(
            model_name='contingent',
            name='members',
            field=models.ManyToManyField(related_name='con_members', to='KYusers.KYProfile'),
        ),
    ]
