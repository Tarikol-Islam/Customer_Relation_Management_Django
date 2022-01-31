from datetime import date
from pyexpat import model
from sqlite3 import DateFromTicks
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

from .models import RawOrder

class RawOrderCreateForm(forms.ModelForm):
    amount_unit = forms.ChoiceField(choices=[('KG','KG'),('Litter','Litter'),('Piece','Piece'),('Dozen','Dozen'),('Inch','Inch'),('Meter','Meter'),('Cluster-4','Hali'),('Feet','Feet')], required=True)
    order_status = forms.ChoiceField(required=False)
    class Meta:
        model = RawOrder
        fields = ['order_status','quantity','amount_unit','asking_price','delivery_date']