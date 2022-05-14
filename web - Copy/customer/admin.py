from django.contrib import admin
from .models import Customer, Complaint_Registration, Feedback, General_Item_Order, Medicinal_Item_Order


class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'pin', 'contact', 'email', 'username']


class AdminComplaint_Registration(admin.ModelAdmin):
    list_display = ['comp_id', 'id', 'lic', 'complaint', 'status', 'date']


class AdminItem_order(admin.ModelAdmin):
     list_display = ['order_no', 'id', 'order_date', 'status']


# Register your models here.

admin.site.register(Customer, AdminCustomer)
admin.site.register(Complaint_Registration, AdminComplaint_Registration)
admin.site.register(Feedback)
admin.site.register(General_Item_Order)
admin.site.register(Medicinal_Item_Order)
#admin.site.register(Item_Order)
