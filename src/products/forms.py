from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your Product title'
        }))
    email = forms.EmailField()
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

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "KKP" in title:
            return forms.ValidationError('This is not a valid title!')
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            return forms.ValidationError('This is not a valid email!')
        return email


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
