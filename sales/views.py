from ast import Delete
from asyncio.windows_events import NULL
from itertools import product
from mimetypes import init
from pyexpat import model
import re
from typing import List
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.template import context
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from core.views import login_success
from sales.forms import OrderCreateForm, OrderUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Order,Company, PriceTable,Product
from django.urls import reverse_lazy


# Create your views here.
#PRice Table Part is here
#order views part
class PriceTableListView(LoginRequiredMixin,ListView):
    model = PriceTable
    success_url = reverse_lazy('price_table_list')
    template_name = 'sales/pricetablelist.html'

class PriceTableCreateView(LoginRequiredMixin, CreateView):
    model = PriceTable
    fields = '__all__'
    success_url = reverse_lazy('price_table_list')
    template_name = 'sales/pricetablecreate.html'

class PriceTableUpdateView(LoginRequiredMixin, UpdateView):    
    model = PriceTable
    fields = '__all__'
    success_url = reverse_lazy('price_table_list')
    template_name = 'sales/pricetableupdate.html'

class PriceTableDeleteView(LoginRequiredMixin, DeleteView):
    model = PriceTable
    fields = '__all__'
    success_url = reverse_lazy('price_table_list')
    template_name = 'sales/pricetabledelete.html'

#ORDER views part
class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    success_url = reverse_lazy('orders_list')
    template_name = 'sales/orders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.name == 'Buyer':
            context['object_list'] = Order.objects.filter(order_creator = self.request.user.id)
        else:context["object_list"] = Order.objects.all()
        return context

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    

class OrderCreateView(LoginRequiredMixin,CreateView):
    model = Order
    form_class = OrderCreateForm
    success_url = reverse_lazy('orders_list')
    template_name = 'sales/orderscreate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] =Product.objects.values_list('product_qty', flat=True).get(pk = self.kwargs.get('pk'))
        return context
    

    def stock_update(pk,order_quantity):
        product = Product.objects.get(pk=pk)
        product.product_qty = product.product_qty-order_quantity
        product.save()
    
    def form_valid(self, form):
        #for Stock update facility
        OrderCreateView.stock_update(self.kwargs.get('pk'), form.cleaned_data['order_qty'])
        #for placing order
        Order = form.save(commit=False)
        Order.order_creator =  self.request.user
        form.instance.order_items = Product.objects.get(pk=self.kwargs.get('pk'))
        form.instance.order_total_price = Product.objects.values_list('product_price', flat=True).get(pk=self.kwargs.get('pk'))* form.cleaned_data['order_qty']
        Order.save()
        form.save()
        return redirect('orders_list')
     
    
# class OrderUpdateView(LoginRequiredMixin, UpdateView):    
#     model = Order
#     fields = ['order_items', 'order_details','order_qty', 'order_status']
#     success_url = reverse_lazy('orders_list')
#     template_name = 'sales/ordersupdate.html'
#     def form_valid(self, form):
        
#         #for Stock update facility
#         # OrderCreateView.stock_update(self.kwargs.get('pk'), form.cleaned_data['order_qty'])
#         #for placing order
        
#         Order = form.save(commit=False)
#         print(self.kwargs.get('order_qty'))
#         print(form.cleaned_data['order_qty'])
#         Order.save()
#         form.save()
        
#         return redirect('orders_list')


# class OrderDeleteView(LoginRequiredMixin, DeleteView):
#     model = Order
#     fields = '__all__'
#     success_url = reverse_lazy('orders_list')
#     template_name = 'sales/ordersdelete.html'

#     def delete(self, *args, **kwargs):
#         print(self.instance.id)
#         print("Hello world")


# @login_required
# def OrderCreate(request,pk):
#     context = {}
#     form = OrderCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("order_list")
#     context['form'] = form
#     return render(request, "sales/orderscreate.html")


class OrderDetailView(LoginRequiredMixin,DetailView):
    model = Order
    template_name = 'sales/orderdetails.html'

@login_required
def OrderUpdate(request, pk):
    context = {}
    obj = get_object_or_404(Order, id = pk)
    product = Product.objects.get(pk = obj.order_items.pk)
    product.product_qty = product.product_qty + obj.order_qty
    form = OrderUpdateForm(request.POST or None, instance = obj)
    if form.is_valid():
        product.product_qty = product.product_qty - form.instance.order_qty
        form.instance.order_total_price =obj.order_items.product_price * obj.order_qty
        product.save()
        form.save()
        return redirect("orders_list")
    context['form'] = form
    return render(request, 'sales/ordersupdate.html', context)

@login_required
def OrderDelete(request, pk):    
    order = get_object_or_404(Order, id = pk)
    context = {'order_name' : order.order_name}
    PDkey = order.order_items.pk
    if request.method == "POST":
        product = Product.objects.get(pk = PDkey)
        product.product_qty = product.product_qty + order.order_qty
        product.save()
        order.delete()
        return HttpResponseRedirect("/")
    return render(request,'sales/ordersdelete.html',context)
    


#company
class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'sales/company.html'

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company_list')
    template_name = 'sales/companycreate.html'

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company_list')
    template_name = 'sales/companyupdate.html'

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company_list')
    template_name = 'sales/companydelete.html'






#Product View part
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    success_url = reverse_lazy('product_list')
    template_name = 'sales/products.html'
    

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    template_name = 'sales/productscreate.html'

class ProductUpdateView(LoginRequiredMixin, UpdateView):    
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    template_name = 'sales/productsupdate.html'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    template_name = 'sales/productsdelete.html'

class ProductDetailView(DetailView):
    model = Product
    fields = '__all__'
    template_name = "sales/productdetails.html"




    

