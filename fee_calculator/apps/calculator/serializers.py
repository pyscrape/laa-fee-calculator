# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import (
    Scheme, Scenario, FeeType, AdvocateType, OffenceClass, Price, Unit, Modifier
)


class SchemeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Scheme
        fields = (
            'id',
            'effective_date',
            'start_date',
            'end_date',
            'suty',
            'description',
        )


class FeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeType
        fields = (
            'name',
            'code',
            'is_basic',
            'units',
            'modifier_units',
        )


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = (
            'id',
            'name',
        )


class AdvocateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateType
        fields = (
            'id',
            'name',
        )


class OffenceClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffenceClass
        fields = (
            'id',
            'name',
            'description',
        )


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = (
            'id',
            'name',
        )


class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = (
            'unit',
            'limit_from',
            'limit_to',
            'modifier_percent',
        )


class PriceFeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeType
        fields = (
            'id',
            'name',
            'code',
            'is_basic',
        )


class PriceSerializer(serializers.ModelSerializer):
    scenario = ScenarioSerializer(read_only=True)
    scheme = SchemeSerializer(read_only=True)
    advocate_type = AdvocateTypeSerializer(read_only=True)
    fee_type = PriceFeeTypeSerializer(read_only=True)
    offence_class = OffenceClassSerializer(read_only=True)
    unit = UnitSerializer(read_only=True)
    modifiers = ModifierSerializer(many=True, read_only=True)

    class Meta:
        model = Price
        fields = (
            'id',
            'scenario',
            'advocate_type',
            'fee_type',
            'offence_class',
            'scheme',
            'unit',
            'fee_per_unit',
            'fixed_fee',
            'limit_from',
            'limit_to',
            'modifiers',
        )
