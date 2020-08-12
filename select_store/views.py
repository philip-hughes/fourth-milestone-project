from django.shortcuts import render
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyA7Y1Jc7Syxl2pf04Y9wIy-HbV26wVkpzo')


def select_store(request):
    if request.POST:
        print("working..................")
        print("request data", request.POST)
    else:
        print('not form request')

    origin = (43.012486, -83.6964149)
    destination = (40.714224, -73.961452)

    distance_response = gmaps.distance_matrix(origin, destination)
    distance = int(distance_response['rows'][0]['elements'][0]['distance']['value'])
    print('Distance response: ', distance_response, 'Distance: ', distance - 1403)

    return render(request, 'select_store/select-store.html')
