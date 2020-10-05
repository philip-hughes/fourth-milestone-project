from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from select_store.models import Store

from .models import Order, OrderLineItem
from menu.models import Product
from django.contrib.auth.models import User

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        billing_details = intent.charges.data[0].billing_details
        order_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the billing details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        #  Check if order has already been created
        order_exists = False
        attempt = 1
        print('wh PID: ', pid)
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    stripe_pid=pid,
                )
                order_exists = True
                print('order exists')
                break
            except Order.DoesNotExist:
                print('order does not exist')
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        else:
            store = Store.objects.get(id=intent.metadata.store_id)
            delivery = intent.metadata.delivery
            order = None
            try:
                user = User.objects.get(email=billing_details.email)
                print('user found: ', user)
            except User.DoesNotExist:
                user = None
                print('user does not exist')
            try:
                print('creating order......')
                order = Order.objects.create(
                    name=billing_details.name,
                    user=user,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    store=store,
                    delivery=delivery,
                    stripe_pid=pid,
                    order_total=order_total
                )
                print('wh cart...', cart)
                for item in json.loads(cart):
                    print('creating line item', item['product_id'])
                    product = Product.objects.get(sku=item['product_id'])
                    print('product found...........')
                    item_price = float(item['item_price'])
                    quantity = int(item['quantity'])
                    sub_total = item_price * quantity
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        size=item['size'],
                        quantity=item['quantity'],
                        lineitem_total=sub_total,
                        customizations=item['customizations']
                    )
                    order_line_item.save()
            except Exception as e:
                print('exception: ', e)
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
