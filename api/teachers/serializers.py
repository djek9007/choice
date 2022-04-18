from rest_framework import serializers

from teachers.models import TeacherProfile


class TeacherSerializer(serializers.ModelSerializer):
    """Вывод всех учителей"""

    class Meta:
        model = TeacherProfile
        exclude = ('created_date', 'edit_date', 'published',)


