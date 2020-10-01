from allauth.account.forms import SignupForm 
from django import forms
from profiles.models import UserProfile


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs) 
        self.auto_id = '%s'

    first_name = forms.CharField(max_length=30, label='First Name')
    contact_number = forms.CharField(max_length=20, label='Contact number')
    search_input = forms.CharField(max_length=200, label='Address' )
    loc_lat = forms.CharField(widget=forms.HiddenInput())
    loc_long = forms.CharField(widget=forms.HiddenInput())

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        contact_number = self.cleaned_data['contact_number']
        customer_address = self.cleaned_data['search_input'].split(',')
        latitude = self.cleaned_data['loc_lat']
        longitude = self.cleaned_data['loc_long']
        print('signup address: ', customer_address)
        user_profile = UserProfile.objects.create(user=user,
                                                  contact_number=contact_number,
                                                  street_address1=customer_address[0],
                                                  street_address2=customer_address[1],
                                                  county=customer_address[2],
                                                  latitude=latitude,
                                                  longitude=longitude)
        user_profile.save()
        return user
