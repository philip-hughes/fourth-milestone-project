from django.shortcuts import render
from cart.contexts import cart_contents
from django.conf import settings
from .forms import OrderForm
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    context_bag = cart_contents(request)
    stripe_total = round(context_bag['total'] * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY
    )

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request):
    template = 'checkout/checkout_success.html'
    context = {
    }

    return render(request, template, context)
