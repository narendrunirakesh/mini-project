from django import forms
from . models import product_adding


class ProductForm(forms.ModelForm):
    class Meta:
        model = product_adding
        fields = ['product_id','product_name', 'product_category', 'product_price']
        #fields='__all__'