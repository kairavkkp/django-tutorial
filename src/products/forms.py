from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your Product title'
        }
    ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"class": "new-class-name two",
                   "rows": 20,
                   "cols": 80,
                   'id': 'my-id-for-text-area'
                   })
    )
    price = forms.DecimalField(initial=199.99)
