from django.shortcuts import get_object_or_404
from menu.models import Pizza


def cart_contents(request):

    cart_items = []
    total = 0
    cart = request.session.get('cart', [])
    print('Context cart: ', cart)

    for item in cart:
        print('context product id: ', item['product_id'])
        pizza = get_object_or_404(Pizza, pk=item['product_id'])
        cart_items.append(pizza)

    context = {
        'cart_items': cart_items,
        'total': total
        }
    print('context:', context)
    return context
