from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inventory(models.Model):
    username=models.CharField(max_length=20)
    P_Type=models.CharField(max_length=20)
    p_Name=models.CharField(max_length=15)
    P_Brand=models.CharField(max_length=10)
    P_Stock=models.IntegerField()
    R_date=models.DateField(null=True,blank=True)
    cost=models.IntegerField()
    P_Size = models.IntegerField()

class Sales(models.Model):
    username=models.CharField(max_length=20)
    customer_name = models.CharField(max_length=40)
    customer_email=models.CharField(max_length=20)
    PS_Type=models.CharField(max_length=20)
    PS_Name=models.CharField(max_length=15)
    PS_Brand=models.CharField(max_length=10)
    QuantitySold=models.IntegerField()
    PS_Date=models.DateField(null=True,blank=True)
    SellingPrice=models.IntegerField()
    PS_Size = models.IntegerField(default = 8)

