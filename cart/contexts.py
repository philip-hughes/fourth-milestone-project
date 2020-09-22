from django.shortcuts import get_object_or_404, redirect, render
from menu.models import Product
from select_store.models import Store


def cart_contents(request):
    store_id = request.session.get('store', '1')
    store = get_object_or_404(Store, pk=store_id)
    cart_items = []
    grand_total = 0
    cart = request.session.get('cart', [])

    print('Context cart: ', cart)

    for item in cart:
        print('context product id: ', item['product_id'])
        product = get_object_or_404(Product, pk=item['product_id'])
        item_price = float(item['item_price'])
        quantity = int(item['quantity'])
        sub_total = item_price * quantity
        item = {
            'product': product,
            'quantity': quantity,
            'sub_total': format(sub_total, '.2f')
        }
        cart_items.append(item)
        grand_total += sub_total

    context = {
        'cart_items': cart_items,
        'grand_total': format(grand_total, '.2f'),
        'store': store,
        }
    print('context:', context)
    return context
