from .models import Product
from django.forms import ModelForm, TextInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "task", "price", "image"]
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



