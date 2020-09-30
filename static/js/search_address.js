var searchInput = 'search_input';

$(document).ready(function () {
    var autocomplete;
    autocomplete = new google.maps.places.Autocomplete((document.getElementById(searchInput)), {
        types: ['geocode'],
        componentRestrictions: {
        country: "IRL"
    }
    });
	
    google.maps.event.addListener(autocomplete, 'place_changed', function (e) {
        if (event.keyCode != 13){
            var near_place = autocomplete.getPlace();
            document.getElementById('loc_lat').value = near_place.geometry.location.lat();
            document.getElementById('loc_long').value = near_place.geometry.location.lng();
        }

    });
});