from django.contrib import admin
from .models import Dealer


class AdminDealer(admin.ModelAdmin):
    list_display = ['lic', 'shop', 'dealer', 'owner', 'city', 'pin', 'contact', 'email', 'username']


# Register your models here.
admin.site.register(Dealer, AdminDealer)
