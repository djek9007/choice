from rest_framework import generics, permissions, viewsets
from .models import Region, District, Locality, TerritorialAffiliation, Language, ClassRoom
from .serializers import RegionSerializer, DistrictSerializer,  LocalitySerializer,  TerritorialAffiliationSerializer, LanguageSerializer, ClassRoomSerializer


class RegionViewSet(viewsets.ModelViewSet):
    """Вывод всех записи область/город из БД"""
    serializer_class = RegionSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Region.objects.filter(published=True)
    # def get_queryset(self):
    #     region = Region.objects.filter(published=True)
    #     return region


class DistrictViewSet(viewsets.ModelViewSet):
    """Вывод всех записи района из БД"""
    serializer_class = DistrictSerializer
    permission_classes = [permissions.AllowAny]
    queryset = District.objects.filter(published=True)

    # def get_queryset(self):
    #     district = District.objects.filter(published=True)
    #     return district


class LocalityViewSet(viewsets.ModelViewSet):
    """Вывод всех записи населенного пункта  из БД"""
    serializer_class = LocalitySerializer
    permission_classes = [permissions.AllowAny]
    queryset = Locality.objects.filter(published=True)
    # def get_queryset(self):
    #     locality = Locality.objects.filter(published=True)
    #     return locality


class TerritorialAffiliationViewSet(viewsets.ModelViewSet):
    """Вывод всех записи территориальной принадлежности  из БД"""
    serializer_class = TerritorialAffiliationSerializer
    permission_classes = [permissions.AllowAny]
    queryset = TerritorialAffiliation.objects.filter(published=True)
    # def get_queryset(self):
    #     territory = TerritorialAffiliation.objects.filter(published=True)
    #     return territory


class LanguageViewSet(viewsets.ModelViewSet):
    """Вывод всех записи языков  из БД"""
    serializer_class = LanguageSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Language.objects.filter(published=True)

    # def get_queryset(self):
    #     language = Language.objects.filter(published=True)
    #     return language


class ClassRoomView(viewsets.ModelViewSet):
    """Вывод всех записи таблицы классов  из БД"""
    serializer_class = ClassRoomSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ClassRoom.objects.filter(published=True)

    # def get_queryset(self):
    #     classRoom = ClassRoom.objects.filter(published=True)
    #     return classRoom

