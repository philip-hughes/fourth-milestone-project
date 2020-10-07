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
        profile_form = UserProfileForm(
            request.POST, instance=profile, prefix="profile")
        if profile_form.is_valid():
            print('form is valid')
            profile_form = profile_form.save()
            user = User.objects.get(email=user.email)
            user.first_name = request.POST['first_name']
            user.email = request.POST['email']
            user.save()
            user = User.objects.get(email=user.email)

            print('saved user: ', user)
            profile_form = UserProfileForm(prefix="profile", initial={
                'user': profile.user,
                'street_address1': profile.street_address1,
                'street_address2': profile.street_address2,
                'county': profile.county,
                'latitude': profile.latitude,
                'longitude': profile.longitude,
                'contact_number': profile.contact_number,
            })
            context = {
                'profile_form': profile_form,
                'user': user
            }
        return render(request, 'profiles/profile.html', context)

    else:
        #user = User.objects.get(email=billing_details.email)
        profile_form = UserProfileForm(prefix="profile", initial={
            'user': profile.user,
            'street_address1': profile.street_address1,
            'street_address2': profile.street_address2,
            'county': profile.county,
            'contact_number': profile.contact_number
        })

        context = {
            'profile_form': profile_form,
            'user': user
        }
        return render(request, 'profiles/profile.html', context)
