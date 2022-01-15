from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title',
                'required': True
            }),
            'display_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select banner image',
                'required': True
            }),
        }