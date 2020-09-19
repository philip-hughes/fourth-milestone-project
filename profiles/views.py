from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.


def profile(request):
    return render(request, 'profiles/profile.html')

