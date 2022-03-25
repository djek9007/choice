from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from django.views.generic.base import View
from rest_framework.views import APIView

# from .forms import OrganizationForm
#
#
#
#
#
#
#
from organizations.forms import OrganizationForm


class OrganizationsView(View):
    def get(self, request):
        form = OrganizationForm

        contex = {
            'form': form,
        }
        return render(request, 'organizations/create.html', contex)


from organizations.models import Organization
from organizations.serializers import OrganizationSerializer, OrganizationDetailSerializer, OrganizationCreateSerializer


class OrganizationCreateViewSet(viewsets.ModelViewSet):
    """Добавление организации"""
    serializer_class = OrganizationCreateSerializer

class OrganizationListView(APIView):
    """Вывод всех организации из БД"""
    def get(self, request):
        organizations = Organization.objects.filter(published=True)
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)



class OrganizationDetailView(APIView):
    """Для детального вывода организации"""
    def get(self, request, pk):
        organization = Organization.objects.get(id=pk, published=True)
        serializer = OrganizationDetailSerializer(organization)
        return Response(serializer.data)