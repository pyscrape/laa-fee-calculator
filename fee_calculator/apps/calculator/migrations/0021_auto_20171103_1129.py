# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0020_feetype_aggregation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocatetype',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feetype',
            name='code',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='feetype',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modifiertype',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='offenceclass',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='price',
            name='fee_per_unit',
            field=models.DecimalField(decimal_places=5, max_digits=12),
        ),
        migrations.AlterField(
            model_name='price',
            name='fixed_fee',
            field=models.DecimalField(decimal_places=5, max_digits=12),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='unit',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]