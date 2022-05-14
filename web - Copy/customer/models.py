import datetime
from django.db import models
from dealer.models import Dealer
from product.models import Product
from doctor.models import Doctor


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.IntegerField()
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8)

    class Meta:
        db_table = "customer"


class General_Item_Order(models.Model):
    order_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    id = models.IntegerField()
    pid = models.IntegerField()
    price = models.IntegerField()
    order_date = models.DateField(default=datetime.date.today)
    qty = models.IntegerField()
    status = models.CharField(max_length=10, default='No')
    deal_id = models.IntegerField(default = 0)
    bill_amount = models.IntegerField(default = 0)

    class Meta:
        db_table = "general_item_order"


class Medicinal_Item_Order(models.Model):
    order_no = models.IntegerField(primary_key=True)
    id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.date.today)
    med_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    qty = models.IntegerField()
    lic = models.IntegerField()
    status = models.BooleanField(default = False)
    allot_status = models.CharField(max_length=100, null=True, blank=True)
    deal_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = "medicinal_item_order"


class Complaint_Registration(models.Model):
    comp_id = models.IntegerField(primary_key=True)
    id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lic = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=200)
    status = models.BooleanField(default = False)
    date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "complaint_registration"


class Feedback(models.Model):
    feed_id = models.IntegerField(primary_key=True)
    id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lic = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    feed = models.CharField(max_length=100)

    class Meta:
        db_table = "feedback"
