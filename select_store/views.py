from django.shortcuts import render
from .models import Store
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyA7Y1Jc7Syxl2pf04Y9wIy-HbV26wVkpzo')


def select_store(request):
    print('link working: ')
    if request.GET:
        print('store name working: ', request.GET['storename'])
        storename = request.GET['storename']
        store = request.session['storeame'] = storename
        print('selected store: ', store)

    if request.POST:
        print("working..................")
        latitude = request.POST['lat']
        longitude = request.POST['long']
        customer_location = (latitude, longitude)
        all_stores = Store.objects.all()
        nearby_stores = []
        distant_stores = []
        for store in all_stores:
            store_location = (store.latitude, store.longitude)
            distance_response = gmaps.distance_matrix(customer_location, store_location)
            store_distance = int(distance_response['rows'][0]['elements'][0]['distance']['value'])
            if store_distance <= 5000:
                nearby_stores.append(store)
            else:
                distant_stores.append(store)
        print('Nearby stores: ', nearby_stores)
        print('Other stores: ', distant_stores)
        context = {
            'nearby_stores': nearby_stores,
            'distant_stores': distant_stores
        }
        return render(request, 'select_store/select-store.html', context)
    else:
        print('not form request')



    return render(request, 'select_store/select-store.html')
