from django import forms 
from .models import *   
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
  email = forms.EmailField(max_length=60,help_text='Required. Add a valid e-mail address')

  class Meta:
    model = Account
    fields = ['email','username','password1','password2','first_name','last_name']
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
          FloatingField('email',
                   'username',
                   'password1',
                   'password2',
                   'first_name',
                   'last_name')
            
          )
     
