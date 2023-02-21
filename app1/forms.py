# forms.py
from django import forms
from .models import Product
from django.core import validators

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), initial='default_name', required=False)
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), validators=[validators.URLValidator()])
    target_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'url', 'target_price']


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username