from dataclasses import fields
from typing import List
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView,View,ListView, UpdateView, DetailView
from django.shortcuts import redirect

from user.filters import SupportFilter
from .forms import SignUpForm, SupportUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import get_user_model
from.models import Support
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView



User = get_user_model()
# Create your views here.

class Home(TemplateView):
    template_name = "basics/home.html"

class Test(TemplateView):
    template_name = "basics/test.html"

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "basics/dashboard.html"
    login_url = reverse_lazy('Login')

class SettingsView(LoginRequiredMixin,TemplateView):
    template_name = 'basics/settings.html'
    login_url = reverse_lazy('Login')


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('Login')
    template_name = 'basics/register.html'



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'basics/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'basics/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('Profile'))

        context = self.get_context_data(user_form=user_form,profile_form=profile_form)

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


##Email verification views part

class SendFormEmail(View):

    def  get(self, request):

        # Get the form data 
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Subject - Django Email Testing', 
            'Hello ' + name + ',\n' + message, 
            'sender@example.com', # Admin
            [
                email,
            ]
        ) 

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('Email') 


class SupportListView(LoginRequiredMixin, FilterView):
    model = Support
    success_url = reverse_lazy('Dashboard')
    template_name = 'support/support_list.html'
    filterset_class = SupportFilter


    
class MySupportListView(LoginRequiredMixin, ListView):
    model = Support
    success_url = reverse_lazy('login_success')
    template_name = 'support/support_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Support.objects.filter(user = self.request.user.id)
        return context    

class SupportCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Support
    fields = ['message']
    success_message = 'Issue Created Successfully'
    template_name = 'support/support_create.html'

    def form_valid(self, form):
        Support = form.save(commit=False)
        Support.user =  self.request.user
        Support.save()
        form.save()
        return redirect('Support_list')

class SupportUpdateView(LoginRequiredMixin, UpdateView):
    model = Support
    form_class = SupportUpdateForm
    success_url = reverse_lazy('Support')
    template_name = 'support/support_update.html'

    def form_valid(self, form):
        Support = form.save(commit=False)
        if form.cleaned_data['admin_reply'] != False:
            Support.status = 'Closed'
        Support.save()

        return redirect('Support')

class SupportDetailView(LoginRequiredMixin,DetailView):
    model = Support
    fields = '__all__'
    template_name = "support/support_details.html"

