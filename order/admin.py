from django.contrib import admin

# Register your models here.
from order.models import StatusOrder, Order, Comment


@admin.register(StatusOrder)
class StatusOrderAdmin(admin.ModelAdmin):
    exclude = ('edit_date',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['organization', 'classroom', 'language', 'publishingHouse', 'countTextBook', 'status', 'sent_raiono', 'sent_uoo', 'published']
    exclude = ('edit_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'order',  'published']
    exclude = ('edit_date',)