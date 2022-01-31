from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.urls import reverse_lazy
# from django.db.models import fields
# from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from pytz import timezone
from user.models import Support
from sales.models import Order
from production.models import RawOrder
from datetime import datetime


# login redirecting part
@login_required
def login_success(request):
    if request.user.groups.name == 'Admin':
        return redirect('Dashboard')
    elif request.user.groups.name == 'Supplier':
        return redirect('raw_materials_list')
    elif request.user.groups.name == 'Buyer':
        return redirect('product_list')


    

    
    
    