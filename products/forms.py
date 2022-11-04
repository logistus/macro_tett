from django import forms
from products.models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_image', 'expiry_date', 'is_macropicks']
        widgets = {
            'expiry_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }
        labels = {
            'product_image': 'Ürün Fotoğrafı',
            'expiry_date': 'TETT',
            'is_macropicks': 'Macropicks'
        }
