from django.shortcuts import render, redirect
from .models import Store
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyA7Y1Jc7Syxl2pf04Y9wIy-HbV26wVkpzo')


def select_store(request):
    print('link working: ')
    if request.GET:
        print('store name working: ', request.GET['store'])
        store_id = request.GET['store']
        delivery = request.GET['delivery']
        request.session['delivery'] = delivery
        store = request.session['store'] = store_id
        print('selected store: ', store)
        return redirect('menu')

    if request.POST:
        latitude = request.POST['lat']
        longitude = request.POST['long']
        if latitude and longitude:
            customer_address = request.POST['customer_address'].split(',')
            print('customer address: ', customer_address)
            customer_address = {
                "street_address1": customer_address[0],
                "street_address2": customer_address[1],
                "county": customer_address[2],
            }
            request.session['customer_address'] = customer_address
            customer_address_coordinates = (latitude, longitude)
            all_stores = Store.objects.all()
            nearby_stores = []
            distant_stores = []
            for store in all_stores:
                store_location = (store.latitude, store.longitude)
                distance_response = gmaps.distance_matrix(
                    customer_address_coordinates, store_location)
                store_distance = int(
                    distance_response['rows'][0]['elements'][0]['distance']['value'])
                if store_distance <= 5000:
                    nearby_stores.append(store)
                else:
                    distant_stores.append(store)
            context = {
                'nearby_stores': nearby_stores,
                'distant_stores': distant_stores
            }
            return render(request, 'select_store/select-store.html', context)
        else:
            context = {
                "invalid_address": True
            }
            return render(request, 'select_store/select-store.html', context)

    return render(request, 'select_store/select-store.html')
