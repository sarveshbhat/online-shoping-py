from django.contrib import admin
from .models import Product


class AdminProduct(admin.ModelAdmin):
    list_display = ['pid', 'name', 'type', 'price', 'unit', 'quality']


# Register your models here.
admin.site.register(Product, AdminProduct)
