from django.contrib import admin

# Register your models here.
from teachers.models import TeacherProfile


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', )
    filter_horizontal = ('language','classroom', 'parallesclass', 'subject')

admin.site.register(TeacherProfile, TeacherAdmin)