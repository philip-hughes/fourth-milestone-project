/*$("#submit-payment").click(function () {
        $('#payment-form').submit()
        console.log('submitting form from other js')
});*/
$("#id_street_address1, #id_street_address2, #id_county").prop("disabled", true)

var form = $('#payment-form');
/*Handle form submit*/
form.submit(function(ev) {
    console.log('submit form in checkout js')
    $("#id_street_address1, #id_street_address2, #id_county").prop("disabled", false)
})

