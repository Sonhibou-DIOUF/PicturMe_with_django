from django import forms
from django.forms import ModelForm
from .models import Transaction

class TransactionForm(forms.Form):
    pass

class TransactionModelForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'