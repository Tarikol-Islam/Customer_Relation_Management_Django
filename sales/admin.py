from django.contrib import admin

from sales.models import Company, Order, PriceTable, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Order)
admin.site.register(PriceTable)