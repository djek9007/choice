from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
# Register your models here.
from catalog.models import Region, District, Locality, TerritorialAffiliation, Language, Subject, ClassRoom
from order.models import Order, StatusOrder, Comment
from role.models import Role, RegionRole, DistrictRole, LocalityRole


class DistrictAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'name', 'region',  ]
    actions = ['unpublish', 'publish', ]
    list_display_links = ("name",)

    # readonly_fields = ('published',)
    exclude = ('edit_date',)

    list_filter = ('region',)

    list_per_page = 20

class RegionAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'name', 'published', ]

    list_display_links = ("name",)

    exclude = ('edit_date',)
    # readonly_fields = ('published',)

    list_per_page = 20


class LanguageAdmin(admin.ModelAdmin):
    exclude = ('edit_date',)



class LocalityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region', 'district', 'published', ]
    exclude = ('edit_date',)
    list_display_links = ('name',)


class TerritorialAffiliationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published', ]
    exclude = ('edit_date',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'language']
    list_filter = ('language',)

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RegionRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'region_role',)

class DistrictRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'region_role', 'district_role',)

class LocalityRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'region_role', 'district_role', 'locality_role',)



class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        #for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list

admin.site = MyAdminSite()
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(TerritorialAffiliation, TerritorialAffiliationAdmin)
admin.site.register(Language, LanguageAdmin)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)




admin.site.register(Role, RoleAdmin)
admin.site.register(RegionRole, RegionRoleAdmin)
admin.site.register(DistrictRole, DistrictRoleAdmin)
admin.site.register(LocalityRole, LocalityRoleAdmin)
admin.site.register(Order)
admin.site.register(StatusOrder)
admin.site.register(Comment)

#Регистрируем стандартные
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)