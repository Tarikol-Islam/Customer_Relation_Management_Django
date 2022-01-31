from django.urls import path
from .views import *

urlpatterns = [
    #listview
    path('rawmaterials/',RawMaterialListView.as_view(),name = 'raw_materials_list'),
    path('raworders/',RawOrderListView.as_view(),name = 'raw_orders_list'),
    path('suppliers/',SupplierListView.as_view(),name = 'suppliers_list'),
    #createview
    path('rawmaterials/create',RawMaterialCreateView.as_view(),name = 'raw_materials_create'),
    path('raworders/create',RawOrderCreateView.as_view(),name = 'raw_orders_create'),
    path('raworders/<int:pk>/create',RawOrderCreateView.as_view(),name = 'raw_orders_create'),
    path('suppliers/create',SupplierCreateView.as_view(),name = 'suppliers_create'),
    #updateview
    path('rawmaterials/<int:pk>/update',RawMaterialUpdateView.as_view(),name = 'raw_materials_update'),
    path('raworders/<int:pk>/update',RawOrderUpdateView.as_view(),name = 'raw_orders_update'),
    path('suppliers/<int:pk>/update',SupplierUpdateView.as_view(),name = 'suppliers_update'),
    #deleteview
    path('rawmaterials/<int:pk>/delete',RawMaterialDeleteView.as_view(),name = 'raw_materials_delete'),
    path('raworders/<int:pk>/delete',RawOrderDeleteView.as_view(),name = 'raw_orders_delete'),
    path('suppliers/<int:pk>/delete',SupplierDeleteView.as_view(),name = 'suppliers_delete'),
    #Details View
    path('rawmaterials/<int:pk>/details',RawMaterialsDetailView.as_view(),name = 'raw_materials_details'),
]
