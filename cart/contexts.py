from django.shortcuts import get_object_or_404, redirect, render
from menu.models import Product
from select_store.models import Store


def cart_contents(request):
    store_id = request.session.get('store', '1')
    customer_address = request.session['customer_address'].split(',')
    customer_address = {
        "street_address1" : customer_address[0],
        "street_address2" : customer_address[1],
        "county" : customer_address[2],
    }
    print('context address: ', customer_address)
    store = get_object_or_404(Store, pk=store_id)
    cart_items = []
    total = 0
    cart = request.session.get('cart', [])

    print('Context cart: ', cart)

    for item in cart:
        print('context product id: ', item['product_id'])
        pizza = get_object_or_404(Product, pk=item['product_id'])
        item_price = float(item['price'])
        cart_items.append(pizza)
        total += item_price

    context = {
        'cart_items': cart_items,
        'total': total,
        'store': store,
        'customer_address': customer_address
        }
    print('context:', context)
    return context
