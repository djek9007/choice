from django.urls import path

from . import views


app_name = 'alt'

urlpatterns = [
    path('', views.AlternativeListView.as_view()),
    path('create/', views.AlternativeCreateView.as_view()),


    # path('', OrganizationsView.as_view(), name = 'home',),



]