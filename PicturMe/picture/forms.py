from django import forms
from django.forms import ModelForm
from .models import Picture

class PictureForm(forms.Form):
    pass

class PictureModelForm(ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'