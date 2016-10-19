# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cccd_fee_type', models.CharField(max_length=10, null=True)),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=150)),
                ('calculation_method', models.PositiveSmallIntegerField()),
                ('case_uplift_allowed', models.NullBooleanField()),
                ('aprt_approval_type', models.PositiveSmallIntegerField(choices=[(1, 'Manual'), (2, 'Validate')])),
                ('cis_transaction_category', models.PositiveSmallIntegerField()),
                ('defendant_uplift_allowed', models.BooleanField()),
                ('enabled', models.BooleanField()),
                ('evid_threshold_amount', models.PositiveSmallIntegerField(null=True)),
                ('hearing_type', models.PositiveSmallIntegerField(choices=[(1, 'Ancillary'), (2, 'Main')], null=True)),
                ('max_claim_value', models.PositiveIntegerField()),
                ('notes', models.TextField(null=True)),
                ('on_indictment', models.NullBooleanField()),
                ('prior_auth_reqd', models.NullBooleanField()),
                ('rate_applicable', models.BooleanField()),
                ('refference_prefix', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=150)),
                ('enabled', models.BooleanField()),
                ('appeal_allowed', models.BooleanField()),
                ('auto_authorise_threshold', models.PositiveSmallIntegerField(null=True)),
                ('auto_authorise_threshold_num', models.PositiveSmallIntegerField(null=True)),
                ('final_bill', models.BooleanField()),
                ('ordering_value', models.PositiveSmallIntegerField()),
                ('recoup_allowed', models.BooleanField()),
                ('vat', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psty_person_type', models.PositiveSmallIntegerField(choices=[(1, 'JRALONE'), (2, 'LEDJR'), (3, 'LEADJR'), (4, 'QC')])),
                ('limit_from', models.PositiveSmallIntegerField()),
                ('limit_to', models.PositiveSmallIntegerField(null=True)),
                ('fee_per_unit', models.PositiveSmallIntegerField()),
                ('unit', models.PositiveSmallIntegerField(choices=[(1, 'Hour'), (2, 'Half day'), (3, 'Day'), (4, 'Case'), (5, 'Fixed')])),
                ('additional_uplift_perc', models.PositiveSmallIntegerField()),
                ('bist_bill_sub_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fees', to='scheme.BillSubType')),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('suty_base_type', models.PositiveSmallIntegerField(choices=[(1, 'Advocate'), (2, 'Solicitor')])),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='fee',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fees', to='scheme.Scheme'),
        ),
        migrations.AddField(
            model_name='billsubtype',
            name='bill_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_types', to='scheme.BillType'),
        ),
    ]
