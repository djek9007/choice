from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from alternative.models import Alternative
from alternative.serializers import AlternativeCreateSerializers, AlternativeListSerializers



class AlternativeListView(APIView):
    """Вывод всех выбранных издательств"""

    def get(self, request):
        alternative = Alternative.objects.filter(published=True)
        serializer = AlternativeListSerializers(alternative, many=True)

        return Response(serializer.data)

class AlternativeCreateView(APIView):
    """Добавление выбранного алтернативного учебника"""
    def post(self, request):
        alternative = AlternativeCreateSerializers(data = request.data)
        if alternative.is_valid():
            alternative.save()
        return  Response(status=201)