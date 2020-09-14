from allauth.account.forms import SignupForm 
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    contact_number = forms.CharField(max_length=20, label='Contact number')


def signup(self, request, user):
    user.first_name = self.cleaned_data['first_name']
    user.contact_number = self.cleaned_data['contact_number']
    user.save()
    return user
