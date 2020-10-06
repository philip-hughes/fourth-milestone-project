from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):
    user = request.user
    print('user details: ', user.email)
    profile = UserProfile.objects.get(user=user)
    print('user profile: ', profile.street_address1)

    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
    else:
        #user = User.objects.get(email=billing_details.email)
        profile_form = UserProfileForm(initial={
            'street_address1': profile.street_address1,
            'street_address2': profile.street_address2,
            'county': profile.county,
            'contact_number': profile.county
        })

        context = {
            'profile_form': profile_form
        }
        return render(request, 'profiles/profile.html', context)
