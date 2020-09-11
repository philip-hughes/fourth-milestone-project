from django.shortcuts import (render, redirect, reverse, HttpResponse)
import json 
from pizza_dojo.utils.decorators import select_store_decorator


@select_store_decorator
def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    print('Adding to cart...')
    size_price = json.loads(request.POST.get('size_price'))
    size = size_price['size']
    price = size_price['price']
    cart = request.session.get('cart', [])
    quantity = request.POST.get('quantity')
    cart.append({'product_id': product_id, 'size': size, 'price': price})


    print('Added to cart: ', cart)
    request.session['cart'] = cart
    return redirect('menu')


def adjust_cart(request, product_id):

    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):

    return HttpResponse(status=200)
