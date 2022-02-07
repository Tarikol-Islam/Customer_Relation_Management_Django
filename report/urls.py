from django.urls import path, include, re_path
# from django.conf.urls import url
from .views import BuyerReportView, DashboardView, MonthlyBenifitCreateView, MonthlyBenifitListView, MonthlyBenifitUpdateView, ProductionReportView, SalesReportView, SearchView, SupplierReportView
urlpatterns = [
    path('salesreport/', SalesReportView.as_view(), name='sales_report'),
    path('productionreport/', ProductionReportView.as_view(), name='production_report'),
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('buyerreport/', BuyerReportView.as_view(), name = 'buyer_report'),
    path('supplierreport/', SupplierReportView.as_view(), name = 'supplier_report'),
    path('search/',SearchView.as_view(),name='search'),
    path('monthlybenifitcreate/', MonthlyBenifitCreateView.as_view(),name='monthlybenifit_create'),
    path('<int:pk>/monthlybenifitupdate/', MonthlyBenifitUpdateView.as_view(), name='monthlybenifit_update'),
    path('monthlybenifitlist/', MonthlyBenifitListView.as_view(),name='monthlybenifit_list'),
]
