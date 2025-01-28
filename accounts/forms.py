from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['nickname', 'email', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nickname")
