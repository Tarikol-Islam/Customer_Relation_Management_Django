from email import message
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div, HTML
from django.contrib.auth import get_user_model
from .models import Support

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required & Unique')
    email = forms.EmailField(max_length=254, required=True, help_text='Enter a Valid Email Address')
    class Meta:
        model = User
        fields =['username','name','email','password1','password2', 'groups', 'photo'          
        ]
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'name', 
            'email', 
        ]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'photo',
            'phone',
            'birthdate',
        ]
class SupportUpdateForm(forms.ModelForm):
    message = forms.CharField(disabled=True)
    class Meta:
        model = Support
        fields = ['message', 'admin_reply' ]

class SupportFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.helper = FormHelper()
            self.helper.form_class = 'form-group'
            self.helper.form_method = 'get'
            self.helper.form_show_lebels= True
            self.helper.layout = Layout(
                Row(
                    Column(HTML("""<h3>Support</h3>"""), css_class = 'form-inline col-md-3 mb-0 text-primary'),
                    Column('user',css_class='form-inline col-md-3 mb-0 h5'),
                    Column('status',css_class='form-inline col-md-3 mb-0 h5'),
                    Column(HTML("""<button class="mx-5 btn btn-md btn-primary">Search</button>"""),css_class='form-inline col-md-3 mb-0')
                    )
            )
            