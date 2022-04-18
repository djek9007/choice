from rest_framework import viewsets


from api.organizations.serializers import OrganizationSerializer
from organizations.models import Organization


class OrganizationsViewSet(viewsets.ModelViewSet):
    """Модель Организации"""
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.filter(published=True)



