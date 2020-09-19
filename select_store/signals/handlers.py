from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
import googlemaps


@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    user = request.user
    print('User logged in from select store.....', user)
