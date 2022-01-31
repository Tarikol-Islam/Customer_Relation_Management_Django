from typing import Pattern
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from .views import *

urlpatterns = [
    #Price Table part
    path('pricetable/',PriceTableListView.as_view(), name = 'price_table_list'),
    path('pricetable/create/',PriceTableCreateView.as_view(), name = 'price_table_create'),
    path('pricetable/<int:pk>/update/',PriceTableUpdateView.as_view(), name = 'price_table_update'),
    path('pricetable/<int:pk>/delete/',PriceTableDeleteView.as_view(), name = 'price_table_delete'),
    #orders part
    path('order/',login_required(OrderListView.as_view()), name = 'orders_list'),
    #path('order/create/',OrderCreateView.as_view(), name = 'orders_create'),
    path('order/<int:pk>/create/',OrderCreateView.as_view(), name = 'orders_create'),
    #path('order/<int:pk>/create/',OrderCreate, name = 'orders_create'),
    # path('order/<int:pk>/update/',OrderUpdateView.as_view(), name = 'orders_update'),
    path('order/<int:pk>/update/',OrderUpdate, name = 'orders_update'),
    #path('order/<int:pk>/delete/',OrderDeleteView.as_view(), name = 'orders_delete'),
    path('order/<int:pk>/delete/',OrderDelete, name = 'orders_delete'),
    path('order/<int:pk>/details/', OrderDetailView.as_view(), name = 'order_details'),

    #Company Part
    path('company/',CompanyListView.as_view(), name = 'company_list'),
    path('company/create/',CompanyCreateView.as_view(), name = 'company_create'),
    path('company/<int:pk>/update/',CompanyUpdateView.as_view(), name = 'company_update'),
    path('company/<int:pk>/delete/',CompanyDeleteView.as_view(), name = 'company_delete'),
    #Product Part
    path('product/',ProductListView.as_view(), name = 'product_list'),
    path('product/<int:pk>/details/',ProductDetailView.as_view(), name = 'product_details'),
    path('product/create/',ProductCreateView.as_view(), name = 'product_create'),
    path('product/<int:pk>/update/',ProductUpdateView.as_view(), name = 'product_update'),
    path('product/<int:pk>/delete/',ProductDeleteView.as_view(), name = 'product_delete'),
]
