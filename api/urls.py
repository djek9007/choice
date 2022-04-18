from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.catalog.router import router as catalog_router
from api.order.router import router as order_router
from api.organizations.router import router as organization_router
from api.role.router import router as role_router
from api.teachers.router import router as teacher_router

from api.catalog.views import LogoutView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/token/verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('api/token/logout/', LogoutView.as_view(), name="auth_logout"),
    path('catalogs/', include(catalog_router.urls)),
    path('orders/', include(order_router.urls)),
    path('organizations/', include(organization_router.urls)),
    path('publishinghouses/', include(organization_router.urls)),
    path('roles/', include(role_router.urls)),
    path('teachers/', include(teacher_router.urls)),

]

