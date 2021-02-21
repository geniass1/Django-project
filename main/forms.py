from .models import Product
from django.forms import ModelForm, TextInput, Select


category_choices = (('books', 'books'),
                    ('clothes', 'clothes'),
                    ('technique', 'technique'))


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "task", "price",  "image", "category"]
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control'
        }),
            "task": TextInput(attrs={
            'class': 'form-control'

        }),
            "price": TextInput(attrs={
            'class': 'form-control'
        }),
            "category": Select(
            choices=category_choices)
        }


