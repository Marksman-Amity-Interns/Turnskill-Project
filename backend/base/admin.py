from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(user)
class user(admin.ModelAdmin):
    list_display = ['id', 'email']
