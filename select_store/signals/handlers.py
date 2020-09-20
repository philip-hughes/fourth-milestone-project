from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from select_store.models import Store
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyA7Y1Jc7Syxl2pf04Y9wIy-HbV26wVkpzo')


@receiver(user_logged_in)
def set_store(sender, user, request, **kwargs):
    if not request.user.is_superuser:
        user_id = request.user.id
        user_profile = get_object_or_404(UserProfile, user=user_id)
        latitude = user_profile.latitude
        longitude = user_profile.longitude
        customer_address = {
            "street_address1": user_profile.street_address1,
            "street_address2": user_profile.street_address2,
            "county": user_profile.street_address2,
        }
        request.session['customer_address'] = customer_address
        customer_address_coordinates = (latitude, longitude)
        all_stores = Store.objects.all()
        nearest_store = {'distance': 5000, 'store': ''}
        for store in all_stores:
            store_location = (store.latitude, store.longitude)
            distance_response = gmaps.distance_matrix(
                customer_address_coordinates, store_location)
            store_distance = int(
                distance_response['rows'][0]['elements'][0]['distance']['value'])
            if store_distance <= nearest_store['distance']:
                nearest_store = {'distance': store_distance, 'store': store}
        request.session['store'] = nearest_store['store'].id
