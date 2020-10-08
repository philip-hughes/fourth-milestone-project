/*Disable address fields on checkout screen, but enable them just before form submission*/
$("#id_street_address1, #id_street_address2, #id_county").prop("disabled", true)
var paymentForm = $('#payment-form');

paymentForm.submit(function(ev) {
    $("#id_street_address1, #id_street_address2, #id_county").prop("disabled", false)
})

