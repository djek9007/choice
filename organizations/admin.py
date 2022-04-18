from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from organizations.models import Organization
from organizations.resources import OrganizationResource


@admin.register(Organization)
class OrganizationAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'region', 'district', 'locality', 'territoriAlaffiliation' ,'published', ]
    exclude = ('edit_date',)
    list_display_links = ('name',)
    resource_class = OrganizationResource
