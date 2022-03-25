from rest_framework import serializers

from teachers.models import TeacherProfile


class TeacherListSerializer(serializers.ModelSerializer):
    """Вывод всех учителей"""
    classroom = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    class Meta:
        model = TeacherProfile
        fields = "__all__"

class TeacherDetailSerializer(serializers.ModelSerializer):
    """Вывод всех учителей"""
    classroom =  serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    subject = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    parallesclass = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = TeacherProfile
        fields = "__all__"


class TeacherCreateSerializers(serializers.ModelSerializer):
    """Добавление пос"""
    class Meta:
        model = TeacherProfile
        fields = "__all__"