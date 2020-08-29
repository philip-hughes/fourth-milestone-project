from django.shortcuts import render
from cart.contexts import cart_contents
from django.conf import settings
import stripe


def checkout(request):
    print('currency: ', settings.STRIPE_CURRENCY)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    context_bag = cart_contents(request)
    stripe_total = round(context_bag['total'] * 100)
    print('secret key: ', stripe_secret_key)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY
    )
    print('Intent: ', intent)
    print('stripe total: ', stripe_total)
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)
