# forms.py
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description']  # Não precisa do 'creator' pois será preenchido automaticamente
