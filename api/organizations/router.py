# # #app order
from rest_framework import routers
from api.organizations.views import OrganizationsViewSet

router = routers.DefaultRouter()

router.register('', OrganizationsViewSet)