from rest_framework import serializers

from .models import TeacherProfile


class TeacherSerializer(serializers.ModelSerializer):
    """Вывод всех учителей"""

    # user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # organization = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # classroom = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    # subject = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    # parallesclass = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    # language = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = TeacherProfile
        exclude = ('created_date', 'edit_date', 'published',)


