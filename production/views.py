from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import redirect


from production.forms import RawOrderCreateForm

from .models import RawMaterial, RawOrder, Supplier

# Create your views here.
# RawMaterial part
class RawMaterialListView(LoginRequiredMixin,ListView):
    model = RawMaterial
    template_name = 'production/rawmaterials.html'
    
class RawMaterialCreateView(LoginRequiredMixin,CreateView):
    model = RawMaterial
    fields = "__all__"
    success_url = reverse_lazy('raw_materials_list')
    template_name = 'production/rawmaterialscreate.html'


class RawMaterialsDetailView(LoginRequiredMixin,DetailView):
    model = RawMaterial
    fields= '__all__'
    template_name = "production/rawmaterialsdetails.html"


class RawMaterialUpdateView(LoginRequiredMixin,UpdateView):
    model = RawMaterial
    fields = '__all__'
    success_url = reverse_lazy('raw_materials_list')
    template_name = 'production/rawmaterialsupdate.html'

class RawMaterialDeleteView(LoginRequiredMixin,DeleteView):
    model = RawMaterial
    fields = '__all__'
    success_url = reverse_lazy('raw_materials_list')
    template_name = 'production/rawmaterialsdelete.html'


# Raw Order Part

class RawOrderListView(LoginRequiredMixin,ListView):
    model = RawOrder
    template_name = 'production/raworders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.name == "Supplier":
            context["object_list"] = RawOrder.objects.filter(order_by = self.request.user.id)
        else:context["object_list"] = RawOrder.objects.all() 
        return context
    

class RawOrderCreateView(LoginRequiredMixin,CreateView):
    model = RawOrder
    form_class = RawOrderCreateForm
    success_url = reverse_lazy('raw_orders_list')
    template_name = 'production/raworderscreate.html'
    
    def form_valid(self, form):
        RawOrder = form.save(commit=False)
        RawOrder.order_by = self.request.user
        RawOrder.item_is = RawMaterial.objects.get(pk= self.kwargs.get('pk'))
        RawOrder.total_price = form.cleaned_data['asking_price'] * form.cleaned_data['quantity']
        RawOrder.save()
        form.save()
        return redirect('raw_orders_list')

class RawOrderUpdateView(LoginRequiredMixin,UpdateView):
    model = RawOrder
    fields = ['order_status','asking_price','quantity','delivery_date']
    success_url = reverse_lazy('raw_orders_list')
    template_name = 'production/rawordersupdate.html'

class RawOrderDeleteView(LoginRequiredMixin,DeleteView):
    model = RawOrder
    fields = '__all__'
    success_url = reverse_lazy('raw_orders_list')
    template_name = 'production/rawordersdelete.html'

#Supplier Part

class SupplierListView(LoginRequiredMixin,ListView):
    model = Supplier
    template_name = 'production/suppliers.html'

class SupplierCreateView(LoginRequiredMixin,CreateView):
    model = Supplier
    fields = '__all__'
    success_url = reverse_lazy('suppliers_list')
    template_name = 'production/supplierscreate.html'

class SupplierUpdateView(LoginRequiredMixin,UpdateView):
    model = Supplier
    fields = '__all__'
    success_url = reverse_lazy('suppliers_list')
    template_name = 'production/suppliersupdate.html'

class SupplierDeleteView(LoginRequiredMixin,DeleteView):
    model = Supplier
    fields = '__all__'
    success_url = reverse_lazy('suppliers_list')
    template_name = 'production/suppliersdelete.html'
