from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(forms.Form):
    pass

class EventModelForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'