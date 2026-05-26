from .models import Module, ModulePrice
from rest_framework import serializers


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ['id', 'name', 'title']


class ModulePriceSerializer(serializers.ModelSerializer):

    module = ModuleSerializer()

    class Meta:
        model = ModulePrice
        fields = '__all__'


class ModulePriceNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModulePrice
        exclude = ['module']


class ModuleDetailSerializer(serializers.ModelSerializer):

    prices = ModulePriceNestedSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Module
        fields = [
            'id',
            'name',
            'title',
            'image',
            'description',
            'prices'
        ]