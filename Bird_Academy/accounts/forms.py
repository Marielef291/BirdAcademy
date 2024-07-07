from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
    # def __init__(self, *args, **kwargs):
    #     super(NewUserForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].help_text = None
    #     self.fields['password1'].help_text = None
    #     self.fields['password2'].help_text = None