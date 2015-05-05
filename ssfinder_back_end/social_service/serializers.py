from rest_framework import serializers

from social_service.models import Category, AACC, Province, Town


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class AACCSerializer(serializers.ModelSerializer):
    class Meta:
        model = AACC
        fields = ('id', 'code', 'name')


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'code', 'name', 'aacc')


class ProvinceWithoutAACCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'code', 'name')


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ('id', 'name', 'province')


class TownWithoutProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ('id', 'name')
