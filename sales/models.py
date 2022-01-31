from email.policy import default
from enum import unique
import random
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django_resized import ResizedImageField
from django.utils import timezone
import datetime
import time
from django.contrib.auth import get_user_model
User = get_user_model()

from user.models import CustomUser
# Create your models here.

class PriceTable(models.Model):
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    rm_price = models.ForeignKey("production.RawMaterial", on_delete=models.CASCADE)
    shipping_cost = models.FloatField(null = True,default=0)
    delivery_cost = models.FloatField(null = True,default=0)
    production_cost = models.FloatField(null=True,default=0)
    others_cost = models.FloatField(null = True,default=0)
    def __str__(self):
        return self.product_id

class Product(models.Model):
    product_name = models.CharField(max_length = 30, null=True)
    product_price = models.FloatField(default = 0, null=True)
    product_desc = models.CharField(max_length = 300, null=True)
    product_qty = models.PositiveIntegerField(default = 1, null=True)
    product_pic = ResizedImageField(upload_to = 'Product/',null=True, blank = True )

    def __str__(self):
        return self.product_name


class Order(models.Model):

    # def new_ref():
    #     not_unique = True
    #     while not_unique:
    #         unique_ref = random.randint(1000000000,9999999999)
    #         if not Order.objects.filter(order_unique_id = unique_ref):
    #             not_unique=False
    #     return str(unique_ref)    

    # order_unique_id = models.CharField(max_length=10,blank=True, editable=False, unique=True,default = new_ref)
    order_name = models.CharField(max_length = 30, null=True)
    order_items = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    order_qty = models.IntegerField(default=1, null=True)
    order_details = models.TextField()
    payment_status = models.BooleanField(default=False)
    order_status_choice = (("New","New"),("Processing","Processing"),("Delivered","Delivered"),("Cancelled","Cancelled"))
    order_status = models.CharField(max_length=10,choices=order_status_choice, default="New")
    order_total_price = models.FloatField(null=True)
    order_date = models.DateField(default= timezone.now)
    delivery_date = models.DateField(null = True)

    
    def __str__(self):
        return self.order_name

    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


class Company(models.Model):
    business_name = models.CharField(max_length = 30, null=False)
    business_address = models.CharField(max_length= 300, null=False)
    business_orders = models.ForeignKey(Order,  on_delete=models.CASCADE, null=True)
    business_bank_account = models.CharField(max_length=30,null=True)
    business_website = models.URLField(default="https://www.",null=True)
    business_email = models.EmailField(null = True, default="business_name@gmail.com")
    business_contact_number = models.CharField(max_length=14,null=True)
    business_contact_person = models.CharField(max_length=80,null=False)
    business_status = models.CharField(max_length=50,null=False, default="National")
    
    def __str__(self):
        return self.business_name


