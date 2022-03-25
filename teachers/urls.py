from django.urls import path

from . import views


app_name = 'teach'

urlpatterns = [
    path('', views.TeacherListView.as_view()),
    path('<int:pk>', views.TeacherDetailView.as_view()),
    path('create/', views.TeacherCreateView.as_view()),
    # path('', OrganizationsView.as_view(), name = 'home',),



]