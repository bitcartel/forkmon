# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20170715_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='highest_diverged_hash',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
