from rest_framework import serializers

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Список организации"""
    # region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # locality = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # territoriAlaffiliation = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # language = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'region', 'district', 'locality', 'territoriAlaffiliation', 'language', 'name',)
