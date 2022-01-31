from email import message
from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, Group


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    last_name = None
    first_name = None
    email = models.EmailField(verbose_name='Email Address')
    name = models.CharField(verbose_name='Full Name', max_length=100)
    photo = models.ImageField(upload_to="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthdate = models.DateField(auto_now_add=False, null=True)
    address = models.CharField(default="None" ,max_length=50)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    phone = PhoneNumberField(unique=True, null = True )
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.username 

class Support(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name=("Issue Creator: "), on_delete=models.CASCADE)
    message = models.CharField(max_length=300,null=False)
    admin_reply = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=10,verbose_name="Issue Status: ",default='New')
