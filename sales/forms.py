from dataclasses import field, fields
from email.policy import default
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.utils import timezone
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_name','order_qty','order_details','order_date',]

class OrderUpdateForm(forms.ModelForm):
    delivery_date = forms.DateField(required=False, help_text='Will be given by the Admin only')
    order_status_choice = (("New","New"),("Processing","Processing"),("Delivered","Delivered"),("Cancelled","Cancelled"))
    order_status = forms.ChoiceField(required=False, choices = order_status_choice)
    order_total_price = forms.FloatField(required=False)
    class Meta:
        model = Order
        fields = ['order_status', 'order_qty','order_details','order_items','delivery_date','order_total_price']