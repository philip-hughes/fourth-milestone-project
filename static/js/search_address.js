var searchInput = "search_input";

$(document).ready(function () {
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
    console.log("setting lat long");
    var near_place = autocomplete.getPlace();
    try {
      document.getElementById('loc_lat').value = near_place.geometry.location.lat();
      document.getElementById('loc_long').value = near_place.geometry.location.lng();
      $("#address-error").prop("hidden", true);
      $("#change-address-button").removeAttr("hidden");
    } catch {
      console.log("Invalid addresss");
    }
  });
  $("#change-address-button").click(function () {
    $("#loc_lat").val("");
    $("#loc_long").val("");
    $("#change-address-button").prop("hidden", true);
    $("#signup_form #search_input").prop("disabled", false).val("");
  });

  $("#signup-submit").click(function (e) {
    $("#search_input").prop("disabled", false);
    e.preventDefault();
    if ($("#loc_lat").val() != ""){ 
        console.log("sumbit form")
        $("#signup_form").submit();
    }
    else {
    $("#address-error").prop("hidden", false);

    }
  });
});
