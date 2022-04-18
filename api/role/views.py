from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.role.serializers import RoleSerializer, RegionRoleSerializer, DistrictRoleSerializer, OrganizationRoleSerializer
from role.models import Role, RegionRole, DistrictRole, OrganizationRole


class RoleViewSet(viewsets.ModelViewSet):
    """Вывод наименование ролей"""
    serializer_class = RoleSerializer
    queryset = Role.objects.filter(published=True)


class RegionRoleViewSet(viewsets.ModelViewSet):
    """для администраторов Области/города"""
    serializer_class = RegionRoleSerializer
    queryset = RegionRole.objects.filter(published=True)


class DistrictRoleViewSet(viewsets.ModelViewSet):
    """для администраторов администраторов района"""
    serializer_class = DistrictRoleSerializer
    queryset = DistrictRole.objects.filter(published=True)


class OrganizationRoleViewSet(viewsets.ModelViewSet):
    """для администраторов  организации"""
    serializer_class = OrganizationRoleSerializer
    queryset = OrganizationRole.objects.filter(published=True)