from django.db import models


# Create your models here.
class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.IntegerField()
    unit = models.IntegerField()
    quality = models.CharField(max_length=100)

    class Meta:
        db_table = "product"
