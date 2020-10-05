from django.shortcuts import (render, redirect, reverse, get_object_or_404)
from cart.contexts import cart_contents
from django.conf import settings
from .models import Order, OrderLineItem
from .forms import OrderForm
import stripe
from select_store.models import Store
from menu.models import Product
from pizza_dojo.utils.decorators import select_store_decorator
import json


@select_store_decorator
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    context_cart = cart_contents(request)
    session_cart = request.session.get('cart', [])
    store_id = request.session['store']
    store = get_object_or_404(Store, pk=store_id)
    
    if request.user.is_anonymous:
        user = None
    else: 
        user = request.user    
    print('User: ', user)
    

    grand_total = float(context_cart['grand_total'])
    delivery = request.session['delivery']

    if request.method == 'POST':
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
            order.store = store
            order.delivery = delivery
            order.order_total = context_cart['grand_total']
            order.stripe_pid = request.POST['pid']
            order.user = user
            order.save()
            for item in context_cart['cart_items']:
                order_line_item = OrderLineItem(
                    order=order,
                    product=item['product'],
                    size=item['size'],
                    quantity=item['quantity'],
                    lineitem_total=item['sub_total'],
                    customizations=item['customizations']
                )
                order_line_item.save()

            return redirect(reverse('checkout_success'))

        else:
            print('invalid form')

    else:
        stripe_total = round(grand_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata={
                'cart': json.dumps(session_cart),
                'delivery': delivery,
                'store_id': store_id,
            }
        )
        pid = intent.id
        print('intent: ', intent)
        customer_address = request.session['customer_address']
        customer_details = request.session.get('customer_details')
        if customer_details:
            order_form = OrderForm(initial={
                'name': customer_details['name'],
                'email': customer_details['email'],
                'phone_number': customer_details['contact_number'],
                'street_address1': customer_address['street_address1'],
                'street_address2': customer_address['street_address2'],
                'county': customer_address['county'],
            })
        else:
            order_form = OrderForm(initial={
                'street_address1': customer_address['street_address1'],
                'street_address2': customer_address['street_address2'],
                'county': customer_address['county'],
            })
        context = {
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'pid': pid,
            'order_form': order_form,
        }
        return render(request, 'checkout/checkout.html', context)


def checkout_success(request):
    template = 'checkout/checkout_success.html'
    context = {
    }

    return render(request, template, context)
