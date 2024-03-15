from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length =100,null =False,blank =False)
    cost_price=models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
    avail_stock=models.IntegerField(null=False,blank=False)
    quantity_sold = models.IntegerField(null=False,blank=False)
    sales= models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
    stock_date=models.DateField(auto_now_add=True)
    sold_date=models.DateField(auto_now=True)

    def __str__(self)->str:
        return self.name