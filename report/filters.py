from django.forms import ChoiceField
from .forms import OrderFilterForm
from sales.models import Order
import django_filters

class OrderFilter(django_filters.FilterSet):
    delivery_date= django_filters.DateFilter()
    class Meta:
        model = Order
        fields = ['delivery_date']
        form = OrderFilterForm