from .models import Product
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "task", "price"]
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control'
        }),
            "task": TextInput(attrs={
            'class': 'form-control'
        }),
            "price": TextInput(attrs={
            'class': 'form-control'
        })
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
