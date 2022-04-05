from rest_framework import generics, permissions, viewsets

from .models import PublishingHouse, TextBook, YearPublising
from .serializers import PublishingHouseSerializer,  TextBookSerializer, YearPublisingSerializer


class PublishingHouseViewSet(viewsets.ModelViewSet):
    """Вывод всех издательств"""
    serializer_class = PublishingHouseSerializer
    permissions = [permissions.AllowAny]
    queryset = PublishingHouse.objects.filter(published=True)


class TextBookViewSet(viewsets.ModelViewSet):
    """Вывод всех учебников"""
    serializer_class = TextBookSerializer
    permissions = [permissions.AllowAny]
    queryset = TextBook.objects.filter(published=True)


class YearPublishingViewSet(viewsets.ModelViewSet):
    """Вывод всех годов издании"""
    serializer_class = YearPublisingSerializer
    permissions = [permissions.AllowAny]
    queryset = YearPublising.objects.filter(published=True)

