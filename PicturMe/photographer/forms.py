from django import forms
from django.forms import ModelForm
from photographer.models import Photographer

class PhotographerForm(forms.Form):
    pass

class PhotographerModelForm(ModelForm):
    class Meta:
        model = Photographer
        fields = '__all__'