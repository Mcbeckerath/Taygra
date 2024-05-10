from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import *


class UsuarioForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'email': EmailInput(), 'password': PasswordInput()}
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'required':'True',
            'placeholder': 'Nome de Usuário',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })

        self.fields['password'].widget.attrs.update({'required':'True',
            'placeholder': 'Senha',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })
        self.fields['email'].widget.attrs.update({'required':'True',
            'placeholder': 'Email',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })
        self.fields['first_name'].widget.attrs.update({'required':'True',
            'placeholder': 'Nome',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })
        self.fields['last_name'].widget.attrs.update({'required':'True',
            'placeholder': 'Sobrenome',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })


class LoginForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'password']
        widgets = {'password': PasswordInput()}    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Usuário',
            'class': 'form-control my-2 p-2',
            'required': True  
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Senha',
            'class': 'form-control my-2 p-2',
            'required': True  
        })
