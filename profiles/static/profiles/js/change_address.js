var searchInput = "search_input";


$(document).ready(function () {
 $("#id_profile-latitude, #id_profile-longitude, .search-wrapper").prop('hidden', 'true')
 $("#id_profile-street_address1, #id_profile-street_address2, #id_profile-county").attr('readonly', 'true')
 
  var autocomplete;
  autocomplete = new google.maps.places.Autocomplete(
    document.getElementById(searchInput),
    {
      types: ["geocode"],
      componentRestrictions: {
        country: "IRL",
      
      },
    }
  );

  google.maps.event.addListener(autocomplete, "place_changed", function () {
    var near_place = autocomplete.getPlace();
    try {
      document.getElementById('id_profile-latitude').value = near_place.geometry.location.lat();
      document.getElementById('id_profile-longitude').value = near_place.geometry.location.lng();
      $("#address-error").prop("hidden", true);
      let addressString = $('#search_input').val().split(',')
      $("#id_profile-street_address1").val(addressString[0])
      $("#id_profile-street_address2").val(addressString[1])
      $("#id_profile-county").val(addressString[2])
      $("#change-address-button").prop("hidden", false);
      $(".search-wrapper").prop("hidden", true).val("");
      addressString = $('#search_input').val("")
    } catch {
      console.log("Invalid addresss");
    }
  });
    $("#change-address-button").click(function () {
    $("#change-address-button").prop("hidden", true);
    $(".search-wrapper").prop("hidden", false).val("");
  });

  $("#apply-changes-button").click(function (e) {
    e.preventDefault();
    if ($("#id_profile-latitude").val() != ""){    
        $("#profile-form").submit();
    }
    else {
    $("#address-error").prop("hidden", false);

    }
  });
});
