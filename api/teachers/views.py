from rest_framework import viewsets, permissions

from teachers.models import TeacherProfile
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """Вывод всех учителей из БД"""
    serializer_class = TeacherSerializer
    queryset = TeacherProfile.objects.filter(published=True)


