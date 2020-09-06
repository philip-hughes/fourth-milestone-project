from django.shortcuts import get_object_or_404
from menu.models import Pizza
from select_store.models import Store


def cart_contents(request):
    cart_items = []
    total = 0
    cart = request.session.get('cart', [])
    store_id = request.session['store']
    store = get_object_or_404(Store, pk=store_id)
    print('Context cart: ', cart)

    for item in cart:
        print('context product id: ', item['product_id'])
        pizza = get_object_or_404(Pizza, pk=item['product_id'])
        item_price = float(item['price'])
        cart_items.append(pizza)
        total += item_price

    context = {
        'cart_items': cart_items,
        'total': total,
        'store': store
        }
    print('context:', context)
    return context
