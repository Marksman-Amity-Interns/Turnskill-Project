from django.contrib import admin
from .models import *
from .resources import CourseResource
# Register your models here.

# @admin.register(user)
# class user(admin.ModelAdmin):
#     list_display = ['id', 'email']
admin.site.register(user)

admin.site.register(feedback)
admin.site.register(video)
admin.site.register(skill)
admin.site.register(notes)
admin.site.register(enrolment)

from import_export.admin import ImportExportModelAdmin

class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
admin.site.register(course,CourseAdmin)