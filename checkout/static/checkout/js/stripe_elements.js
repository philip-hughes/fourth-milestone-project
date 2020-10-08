var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

var form = document.getElementById('payment-form');

/*Handle form submit*/
form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({'disabled': true});
  $('#submit-button').attr('disabled', true)
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
      billing_details: {
        name: $.trim(form.name.value),
        phone: $.trim(form.phone_number.value),
        email: $.trim(form.email.value),
        address: {
            line1:$.trim(form.street_address1.value),
            line2:$.trim(form.street_address2.value),
            state:$.trim(form.county.value),
        }
    },
    }
  }).then(function(result) {
    if (result.error) {
      card.update({'disabled': false});
      $('#submit-button').attr('disabled', false)   
    } else {
      /*The payment has been processed.  Submit the form for order completion.*/
      if (result.paymentIntent.status === 'succeeded') {

        form.submit();
      }
    }
  });
});