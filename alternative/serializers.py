from rest_framework import serializers

from alternative.models import Alternative


class AlternativeListSerializers(serializers.ModelSerializer):
    """Вывод всех выбранных издательств"""
    publishingHouse = serializers.SlugRelatedField(slug_field='name', read_only=True)
    subject = serializers.SlugRelatedField(slug_field='name', read_only=True)
    classroom = serializers.SlugRelatedField(slug_field='name', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    yearPublishing = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Alternative
        fields = "__all__"

class AlternativeCreateSerializers(serializers.ModelSerializer):
    """Добавление пос"""
    class Meta:
        model = Alternative
        fields = "__all__"

    def create(self, validated_data):
        alternative = Alternative.objects.update_or_create(

        )