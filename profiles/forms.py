from django import forms
from .models import UserAddress


class OrderForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('user', 'street_address1', 'street_address2', 'county',)
