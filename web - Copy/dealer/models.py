from django.db import models


# Create your models here.
class Dealer(models.Model):
    lic = models.IntegerField(primary_key=True)
    shop = models.CharField(max_length=100)
    dealer = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.IntegerField()
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8)

    class Meta:
        db_table = "dealer"

    def __str__(self):
        return self.shop
