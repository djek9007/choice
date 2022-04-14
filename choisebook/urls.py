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
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from catalog.views import LogoutView
from .router import router

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



def front(request):
    context = { }
    return render(request, "index.html", context)

schema_view = get_schema_view(
   openapi.Info(
      title="Выбор алтернативных учебников",
      default_version='v1',
      description="Система для выбора алтернативных учебников",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="o.bekzhanov@bmso.kz"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/token/verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('api/token/logout/', LogoutView.as_view(), name="auth_logout"),



    # path('', front),
    # re_path("(?:.*)/", front),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += doc_urls




admin.site.site_header = "Система выбора учебников"
admin.site.site_title = "Администратор"
admin.site.index_title = "Добро пожаловать в систему"