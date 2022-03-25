from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from teachers.models import TeacherProfile
from teachers.serializers import TeacherListSerializer, TeacherDetailSerializer, TeacherCreateSerializers


class TeacherListView(APIView):
    """Вывод всех учителей из БД"""
    def get(self, request):
        teachers = TeacherProfile.objects.filter(published=True)
        serializer = TeacherListSerializer(teachers, many=True)
        return Response(serializer.data)

class TeacherDetailView(APIView):
    """Вывод одного учителя из БД"""

    def get(self, request, pk):
        teachers = TeacherProfile.objects.filter(id=pk, published=True)
        serializer = TeacherDetailSerializer(teachers, many=True)
        return Response(serializer.data)


class TeacherCreateView(APIView):
    """Добавление профиля учителя"""

    def post(self, request):
        teacher = TeacherCreateSerializers(data=request.data)
        if teacher.is_valid():
            teacher.save()
        return Response(status=201)