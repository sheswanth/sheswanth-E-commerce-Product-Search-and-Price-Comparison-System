from django import forms
from .models import Product


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Product
        field = "__all__"
        exclude = ["id"]