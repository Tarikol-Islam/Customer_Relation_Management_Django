from django.urls import path, include, re_path
# from django.conf.urls import url
from .views import BuyerReportView, DashboardView, ProductionReportView, SalesReportView, SupplierReportView
urlpatterns = [
    path('salesreport/', SalesReportView.as_view(), name='sales_report'),
    path('productionreport/', ProductionReportView.as_view(), name='production_report'),
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('buyerreport/', BuyerReportView.as_view(), name = 'buyer_report'),
    path('supplierreport/', SupplierReportView.as_view(), name = 'supplier_report')
]
