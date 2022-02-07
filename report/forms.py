from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div, HTML
class OrderFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.helper = FormHelper()
            self.helper.form_class = 'form-inline'
            self.helper.form_method = 'get'
            self.helper.form_show_lebels= True
            self.helper.layout = Layout(
                Div(
                    Div(HTML("""<h3>Report</h3>"""), css_class = 'form-inline col-md-2 mb-0 text-primary'),
                    Div('delivery_date',css_class='form-inline col-md-6 mb-0 h5 text-left text-black'),
                    Div(HTML("""<button class="mx-5 btn btn-md btn-primary">Search</button>"""),css_class='form-inline col-md-1 mb-0'),
                    css_class = 'row '
                    )
            )
            