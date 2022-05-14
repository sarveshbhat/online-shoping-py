from django.contrib import admin
from .models import Doctor


class AdminDoctor(admin.ModelAdmin):
    list_display = ['lic', 'name', 'specialist', 'clinic', 'city', 'pin', 'contact', 'email', 'username']


# Register your models here.
admin.site.register(Doctor, AdminDoctor)
