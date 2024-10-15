from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'id': 'id_username',
            'name': 'username',
            'placeholder': 'Nom d\'utilisateur',
        })
        self.fields['email'].widget.attrs.update({
            'id': 'id_email',
            'name': 'email',
            'placeholder': 'Adresse email',
        })
        self.fields['password1'].widget.attrs.update({
            'id': 'id_password1',
            'name': 'password1',
            'placeholder': 'Mot de passe',
        })
        self.fields['password2'].widget.attrs.update({
            'id': 'id_password2',
            'name': 'password2',
            'placeholder': 'Confirmer le mot de passe',
        })
