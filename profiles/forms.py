from django import forms
from .models import UserProfile


class UserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'street_address1', 'street_address2', 'county', 'contact_number')
