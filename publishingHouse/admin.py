from django.contrib import admin

# Register your models here.
from publishingHouse.models import PublishingHouse, TextBook, YearPublising


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class YearPublisingAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TextBookAdmin(admin.ModelAdmin):
    list_display = ('publishingHouse', 'subject', 'classroom', 'yearPublishing',)
    list_filter = ('publishingHouse', 'subject', 'classroom', 'yearPublishing',)

admin.site.register(TextBook, TextBookAdmin)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(YearPublising, YearPublisingAdmin)
