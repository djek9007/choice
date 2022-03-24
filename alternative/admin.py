from django.contrib import admin

# Register your models here.
from alternative.models import Alternative


class AlternativeAdmin(admin.ModelAdmin):
    list_display = ('user', 'publishingHouse', 'classroom', 'subject', 'yearPublishing',)

admin.site.register(Alternative, AlternativeAdmin)