from django.shortcuts import (render, redirect, reverse, get_object_or_404)
from cart.contexts import cart_contents
from django.conf import settings
from .forms import OrderForm
import stripe
from select_store.models import Store
from pizza_dojo.utils.decorators import select_store_decorator


@select_store_decorator
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        print('THis is a POST request')
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            store_id = request.session['store']
            order.store = get_object_or_404(Store, pk=store_id)
            order.save()
            return redirect(reverse('checkout_success'))

        else:
            print('invalid form')

    else:
        print('THis is NOT a POST request')
        context_bag = cart_contents(request)
        stripe_total = round(context_bag['total'] * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        order_form = OrderForm()
        context = {
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'order_form': order_form,
        }
        return render(request, 'checkout/checkout.html', context)


def checkout_success(request):
    template = 'checkout/checkout_success.html'
    context = {
    }

    return render(request, template, context)
