# # #app order
from rest_framework import routers

from api.role.views import RoleViewSet, RegionRoleViewSet, DistrictRoleViewSet, OrganizationRoleViewSet

router = routers.DefaultRouter()

router.register('role', RoleViewSet)
router.register('region/role', RegionRoleViewSet)
router.register('district/role', DistrictRoleViewSet)
router.register('organization/role', OrganizationRoleViewSet)