from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['nickname', 'email', 'password']

class LoginForm(forms.Form):  # Modificando para não herdar diretamente de AuthenticationForm
    nickname = forms.CharField(label="Nickname", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
