# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-24 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0021_auto_20171103_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offenceclass',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='offenceclass',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]