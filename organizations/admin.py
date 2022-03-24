from django.contrib import admin

# Register your models here.
from organizations.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region', 'district', 'locality', 'territoriAlaffiliation' ,'published', ]
    exclude = ('edit_date',)
    list_display_links = ('name',)

admin.site.register(Organization, OrganizationAdmin)