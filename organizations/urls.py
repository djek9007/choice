from django.urls import path

from .views import  OrganizationsView

app_name = 'org'

urlpatterns = [

    path('', OrganizationsView.as_view(), name = 'home',),



]