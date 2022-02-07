from dataclasses import fields
from datetime import date, datetime
from itertools import product
from pyexpat import model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template import context
# from django.urls import reverse_lazy
# from django.db.models import fields
# from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from report.models import MonthlyBenifit
from user.models import Support
from sales.models import Company, Order, Product
from production.models import RawOrder, Supplier
from datetime import datetime
from .filters import OrderFilter
from django_filters.views import FilterView
# Create your views here.
#Dashboard part
class SearchView(LoginRequiredMixin,TemplateView):
    template_name = "sales/products.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.filter(product_name__icontains = self.request.GET.get('search',''))
        return context

class DashboardView(LoginRequiredMixin ,TemplateView):
    template_name = "report/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Product Order
        context["all_product_order"] = len(Order.objects.all())
        context["new_product_order"] = len(Order.objects.filter(order_status = 'New'))
        context["processing_product_order"] = len(Order.objects.filter(order_status = 'Processing'))
        context["delivered_product_order"] = len(Order.objects.filter(order_status = 'Delivered'))
        #Raw Order Part
        context["all_raw_order"] = len(RawOrder.objects.all())
        context["new_raw_order"] = len(RawOrder.objects.filter(order_status = 'New'))
        #Support Part
        context["new_support_issues"] = len(Support.objects.filter(status = 'New') )

        #Montly order part
        this_month_first_day = datetime.today().date().replace(day=1)#Fisrt day of any month
        ThisMonthOrders = Order.objects.filter(order_date__gte = this_month_first_day).filter(order_status = 'Delivered' or 'Completed').values('order_total_price')
        Sum = 0
        for data in ThisMonthOrders:
            Sum = Sum+data['order_total_price']
        context['monthly_sell']=Sum

        #Montly Raw Order confirmed
        ThisMonthRawORders = RawOrder.objects.filter(delivery_date__gte = this_month_first_day).filter(order_status = 'Received' or 'Paid').values('total_price')
        Sum = 0
        for data in ThisMonthRawORders:Sum=Sum+data['total_price']
        context['monthly_buy'] = Sum

        #Earnings Overview line graph
        PreviousYear = datetime.today().year-1
        context['year'] = PreviousYear
        #ThisMonth = datetime.today().month
        Earnings = MonthlyBenifit.objects.filter(year = PreviousYear).values_list('month','earnings')
        for month, earnings in Earnings:context["month"+str(month)] = earnings
        
        return context

class SalesReportView(LoginRequiredMixin, TemplateView):
    template_name = "report/salesreport.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        yearmonth = self.request.GET.get('month')
        if yearmonth == None:
            yearmonth = datetime.today().replace(day=1,month=(datetime.today().month-1))
            context["object_list"] = Order.objects.filter(order_status = "Delivered").filter(delivery_date__gte = yearmonth)
        else:
            starting = str(yearmonth)+"-01"
            if yearmonth[5:] != "12":
                ending = str(yearmonth.replace(yearmonth[5:],str(int(yearmonth[5:])+1)))+"-01"
            else:
                ending=str(yearmonth.replace(yearmonth[:4],str(int(yearmonth[:4])+1)))+"-01"
                ending = ending.replace("12","01")
            context ["object_list"] = Order.objects.filter(order_status = "Delivered").filter(delivery_date__gte = starting).filter(delivery_date__lt = ending)
            context["monthly_sell"] = 0
            for price in context["object_list"]:
                context["monthly_sell"] = context["monthly_sell"] + price.order_total_price
            print(context["monthly_sell"])
        return context
    

class BuyerReportView(LoginRequiredMixin, ListView):
    model = Company
    template_name = "report/buyerreport.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = "object_list"
        return context
    

class ProductionReportView(LoginRequiredMixin, ListView):
    model = RawOrder
    template_name = "report/productionreport.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = "object_list"
        return context
    
class SupplierReportView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = "report/supplierreport.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = "object_list"
        return context

class MonthlyBenifitListView(LoginRequiredMixin, ListView):
    model = MonthlyBenifit
    template_name = "report/monthlybenifitlist.html"
    
class MonthlyBenifitCreateView(LoginRequiredMixin, CreateView):
    model = MonthlyBenifit
    fields = '__all__'
    template_name = "report/monthlybenifitcreate.html"

class MonthlyBenifitUpdateView(LoginRequiredMixin, UpdateView):
    model = MonthlyBenifit
    fields = '__all__'
    template_name = "report/monthlybenifitupdate.html"




    

