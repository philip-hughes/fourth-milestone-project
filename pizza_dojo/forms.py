from allauth.account.forms import SignupForm 
from django import forms
from profiles.models import UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    contact_number = forms.CharField(max_length=20, label='Contact number')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.contact_number = self.cleaned_data['contact_number']

        user_profile = UserProfile.objects.create(user=user, contact_number=user.contact_number)
        user_profile.save()

        print('signup request------: ', user.contact_number)
        return user
