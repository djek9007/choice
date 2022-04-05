from rest_framework import serializers
from .models import Region, District, Locality, TerritorialAffiliation, Language, ClassRoom


class RegionSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Область/город"""
    class Meta:
        model = Region
        fields = ('name',)


class DistrictSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Района"""
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = District
        fields = ('id', 'name', 'region',)


class LocalitySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели населенного пункта"""

    class Meta:
        model = Locality
        fields = ('id',  'region', 'district', 'name',)


class TerritorialAffiliationSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели территориальной принадлежности"""

    class Meta:
        model = TerritorialAffiliation
        fields = ('id', 'name',)


class LanguageSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели язык"""

    class Meta:
        model = Language
        fields = ('id', 'name',)


class ClassRoomSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода всех классов"""

    class Meta:
        model = ClassRoom
        fields = ('id', 'name',)