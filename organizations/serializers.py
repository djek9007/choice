from rest_framework import serializers

from .models import Organization

class OrganizationCreateSerializer(serializers.ModelSerializer):
    """Добавление организации"""
    # region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # locality = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # territoriAlaffiliation = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Organization
        fields = "__all__"

class OrganizationSerializer(serializers.ModelSerializer):
    """Список организации"""
    class Meta:
        model = Organization
        fields = ('region', 'district', 'locality', 'territoriAlaffiliation', 'language', 'name',)

class OrganizationDetailSerializer(serializers.ModelSerializer):

    """Для детального вывода организации"""

    region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    locality = serializers.SlugRelatedField(slug_field='name', read_only=True)
    territoriAlaffiliation = serializers.SlugRelatedField(slug_field='name', read_only=True)
    language = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Organization
        fields = ('region', 'district', 'locality', 'territoriAlaffiliation', 'language', 'name',)

