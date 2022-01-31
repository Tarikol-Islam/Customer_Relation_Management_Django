
from django.contrib import admin

from production.models import RawMaterial, RawOrder, Supplier

# Register your models here.
admin.site.register(Supplier)
admin.site.register(RawMaterial)
admin.site.register(RawOrder)