from django.db import models


# Create your models here.
class Doctor(models.Model):
    lic = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    specialist = models.CharField(max_length=100)
    clinic = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.IntegerField()
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "doctor"
