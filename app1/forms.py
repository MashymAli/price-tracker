# forms.py
from django import forms
from .models import Product
from django.core import validators


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), initial='default_name', required=False)
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), validators=[validators.URLValidator()])
    target_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'url', 'target_price']