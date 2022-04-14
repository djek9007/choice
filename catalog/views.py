from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from .models import Region, District, Locality, TerritorialAffiliation, Language, ClassRoom
from .serializers import RegionSerializer, DistrictSerializer,  LocalitySerializer,  TerritorialAffiliationSerializer, LanguageSerializer, ClassRoomSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters import rest_framework as filters
#SimpleJWT token logout
class LogoutView(APIView):
    permission_classes = []

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            data = {"detail": "Token was deleted"}
            return Response(data, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            data = {"detail": str(e)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)



class RegionViewSet(viewsets.ModelViewSet):
    """Вывод всех записи область/город из БД"""
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class DistrictViewSet(viewsets.ModelViewSet):
    """Вывод всех записи района из БД"""
    queryset = District.objects.all()
    serializer_class = DistrictSerializer




class LocalityViewSet(viewsets.ModelViewSet):
    """Вывод всех записи населенного пункта  из БД"""
    serializer_class = LocalitySerializer
    queryset = Locality.objects.filter(published=True)



class TerritorialAffiliationViewSet(viewsets.ModelViewSet):
    """Вывод всех записи территориальной принадлежности  из БД"""
    serializer_class = TerritorialAffiliationSerializer
    queryset = TerritorialAffiliation.objects.filter(published=True)
    # def get_queryset(self):
    #     territory = TerritorialAffiliation.objects.filter(published=True)
    #     return territory


class LanguageViewSet(viewsets.ModelViewSet):
    """Вывод всех записи языков  из БД"""
    serializer_class = LanguageSerializer
    queryset = Language.objects.filter(published=True)

    # def get_queryset(self):
    #     language = Language.objects.filter(published=True)
    #     return language


class ClassRoomView(viewsets.ModelViewSet):
    """Вывод всех записи таблицы классов  из БД"""
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.filter(published=True)

    # def get_queryset(self):
    #     classRoom = ClassRoom.objects.filter(published=True)
    #     return classRoom

