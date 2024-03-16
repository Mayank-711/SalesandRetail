from django.db import models

# Create your models here.
class Inventory(models.Model):
    username=models.CharField(max_length=20)
    P_Type=models.CharField(max_length=20)
    p_Name=models.CharField(max_length=15)
    P_Brand=models.CharField(max_length=10)
    P_Stock=models.IntegerField()
    R_date=models.DateField(null=True,blank=True)
    cost=models.IntegerField()