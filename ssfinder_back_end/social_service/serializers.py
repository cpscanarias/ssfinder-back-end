from rest_framework import serializers

from social_service.models import Category, AACC, Province, Town, \
    SocialService


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


class SocialServiceSerializer(serializers.ModelSerializer):
    province = serializers.ReadOnlyField(source='town.province.name')
    town = serializers.ReadOnlyField(source='town.name')
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = SocialService
        fields = ('id', 'name', 'categories', 'address', 'postal_code', 
            'province', 'town', 'phone', 'email', 'description', 'web', 
            'facebook', 'twitter', 'instagram', 'google_plus', 'tumblr'
        )


class SocialServiceSummarySerializer(serializers.ModelSerializer):
    province = serializers.ReadOnlyField(source='town.province.name')
    town = serializers.ReadOnlyField(source='town.name')
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    
    class Meta:
        model = SocialService
        fields = ('id', 'name', 'categories', 'town', 'province', 'web', 
            'facebook', 'twitter', 'instagram', 'google_plus', 'tumblr'
        )


class SocialServiceAddressSerializer(serializers.ModelSerializer):
    province = serializers.ReadOnlyField(source='town.province.name')
    town = serializers.ReadOnlyField(source='town.name')
    
    class Meta:
        model = SocialService
        fields = ('name', 'address', 'postal_code', 'town', 'province',
            'phone',
        )
