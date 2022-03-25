from django.urls import path

from . import views


app_name = 'org'

urlpatterns = [
    path('', views.OrganizationListView.as_view()),
    path('<int:pk>/', views.OrganizationDetailView.as_view()),
    path('create/', views.OrganizationCreateViewSet.as_view({'post': 'create'})),

    # path('', OrganizationsView.as_view(), name = 'home',),



]