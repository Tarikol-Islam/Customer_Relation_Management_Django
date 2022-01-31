from dataclasses import fields
from random import choice

from django.forms import ChoiceField
from .forms import SupportFilterForm
from .models import Support
import django_filters

class SupportFilter(django_filters.FilterSet):
    status= django_filters.ChoiceFilter(choices = (('New','New'),('Processing','Processing'),('Closed','Closed')))
    class Meta:
        model = Support
        fields = ['user','status']
        form = SupportFilterForm
