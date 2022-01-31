from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('test/', Test.as_view(), name='Test'),
    path('email/', TemplateView.as_view(template_name="basics/email.html"), name='Email'),
    path('signup/', SignUpView.as_view(), name='SignUp'),
    path('login/', auth_views.LoginView.as_view(template_name="basics/login.html"), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='Login'), name='Logout'),
    path('support/',SupportListView.as_view(),name = 'Support_list'),
    path('mysupportlist/',MySupportListView.as_view(),name = 'My_issues'),
    path('support/create/',SupportCreateView.as_view(),name = 'Support_create'),
    path('support/<int:pk>/update/',SupportUpdateView.as_view(),name = 'Support_update'),
    path('support/<int:pk>/details/',SupportDetailView.as_view(),name = 'Support_details'),
    path('settings/', auth_views.PasswordChangeView.as_view(template_name="basics/settings.html", success_url='Dashboard'), name='Settings'),
    path('settings/', SettingsView.as_view(), name='Settings'),
    path('password-reset/',auth_views.PasswordResetView.as_view(
             template_name='basics/password-reset/password_reset.html',
             subject_template_name='basics/password-reset/password_reset_subject.txt',
             email_template_name='basics/password-reset/password_reset_email.html',
             # success_url='/Login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='basics/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='basics/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='basics/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('profile-update/', ProfileUpdateView.as_view(), name='Profile-update'),
    path('profile/', ProfileView.as_view(), name='Profile'),
    path('oauth/', include('social_django.urls', namespace='Social')),
    # path('api/', include('user.api.urls'))

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    