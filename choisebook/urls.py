"""choisebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render

from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static



from api.catalog.views import LogoutView
# from .router import router

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



def front(request):
    context = { }
    return render(request, "index.html", context)




urlpatterns = [

    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include('api.urls')),
    # path('', front),
    # re_path("(?:.*)/", front),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += doc_urls




admin.site.site_header = "Система выбора учебников"
admin.site.site_title = "Администратор"
admin.site.index_title = "Добро пожаловать в систему"