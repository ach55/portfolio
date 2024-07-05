from django import forms
from django.core.validators import EmailValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='')
    email = forms.CharField(label='', validators=[EmailValidator()])
    subject = forms.CharField(max_length=100, label='')
    message = forms.CharField(widget=forms.Textarea, label='')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('name', placeholder='Name'),
            Field('email', placeholder='Email'),
            Field('subject', placeholder='Subject'),
            Field('message', placeholder='Message'),
            Submit('submit', 'Submit', css_class='btn-success')
        )