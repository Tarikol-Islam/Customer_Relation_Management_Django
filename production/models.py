from contextlib import redirect_stderr
from django.db import models
from sales.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50,null=False)
    supplier_bio = models.TextField(max_length=500, blank=True)
    supplier_address = models.TextField(max_length=200, blank=True, null=True)
    supplier_contact =models.CharField(max_length=14, blank=True)
    supplier_birthdate= models.DateField(null=True, blank=True)
    supplier_supply = models.TextField()
    supplier_img= models.ImageField(default='avatar.png', upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % (self.supplier_name, self.supplier_supply)

#The materials a company need for
class RawMaterial(models.Model):
    raw_name = models.CharField(max_length=50, null=False)
    raw_description = models.TextField()
    raw_qty = models.IntegerField()
    raw_qty_unit = models.CharField(max_length=20,null=False, default='Measurement Unit')

    def __str__(self) -> str:
        return self.raw_name
    

#The Materials that moved/request to sell
class RawOrder(models.Model):
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)
    item_is = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    asking_price = models.FloatField(verbose_name="Asking Price Per Unit")
    total_price = models.FloatField(verbose_name = "Total Price", default=0)
    quantity = models.FloatField(null = True) 
    amount_unit = models.CharField(max_length=10, default='KG')
    order_status = models.CharField(max_length=10,null = False,choices=(('Cancelled','Cancelled'),('Processing','Processing'),('Paid','Paid'),('Received','Received')) ,default="New")
    delivery_date = models.DateField(verbose_name="Possible Delivery Date", null=True)

    def __str__(self) -> str:
        return self.item_is.raw_name

class TotalCost(models.Model):
    pass

