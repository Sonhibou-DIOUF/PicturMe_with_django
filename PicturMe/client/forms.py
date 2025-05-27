from django import forms
from django.forms import ModelForm
from .models import Client

class ClientForm(forms.Form):
    pass
class ClientModelForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'