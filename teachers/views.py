from rest_framework import viewsets, permissions

from .models import TeacherProfile
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """Вывод всех учителей из БД"""
    serializer_class = TeacherSerializer
    permissions = [permissions.AllowAny]
    queryset = TeacherProfile.objects.filter(published=True)


