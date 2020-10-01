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
            console.log("setting lat long")
            var near_place = autocomplete.getPlace();
            try {
                document.getElementById('loc_lat').value = near_place.geometry.location.lat();
                document.getElementById('loc_long').value = near_place.geometry.location.lng();
                $('#change-address-button').removeAttr('hidden')
                $('#search_input').prop('disabled', true)
                
            }
            catch {
                console.log('Invalid addresss')
            }
    });
    $('#change-address-button').click(function(){
                $('#loc_lat').val("")
                $('#loc_long').val("")
                $('#change-address-button').prop('hidden', true)
                $('#search_input').prop('disabled', false).val("")
    });

});

