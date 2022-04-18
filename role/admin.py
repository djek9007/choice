from django.contrib import admin

# Register your models here.
from role.models import Role, RegionRole, DistrictRole, OrganizationRole


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(RegionRole)
class RegionRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'region_role',)


@admin.register(DistrictRole)
class DistrictRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'region_role', 'district_role',)


@admin.register(OrganizationRole)
class OrganizationRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'region_role', 'district_role', 'organizations',)
