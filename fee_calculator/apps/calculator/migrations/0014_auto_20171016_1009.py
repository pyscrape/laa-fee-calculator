# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0013_auto_20171016_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='modifiers',
            field=models.ManyToManyField(related_name='prices', to='calculator.Modifier'),
        ),
    ]
