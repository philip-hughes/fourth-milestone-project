from django.shortcuts import (render, redirect, reverse, HttpResponse)
import json 
from pizza_dojo.utils.decorators import select_store_decorator


@select_store_decorator
def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    size_price = json.loads(request.POST.get('size_price'))
    size = size_price['size']
    price = size_price['price']
    product_type = request.POST.get('product_type')
    quantity = int(request.POST.get('quantity'))
    if product_type == 'PIZZA':
        cart.extend([{'product_id': product_id, 'size': size, 'item_price': price, 'quantity': 1}] * quantity)
        request.session['cart'] = cart
        return redirect('menu')

    if cart == []:
        cart.append({'product_id': product_id, 'size': size, 'item_price': price, 'quantity': quantity})
        request.session['cart'] = cart
        return redirect('menu')
    else:    
        for index, item in enumerate(cart):
            if (item['product_id'] == product_id) and (item['size'] == size):
                cart[index]['quantity'] += quantity
                request.session['cart'] = cart
                return redirect('menu')

    cart.append({'product_id': product_id, 'size': size, 'item_price': price, 'quantity': quantity})
    request.session['cart'] = cart
    return redirect('menu')

              

                


    print('Added to cart: ', cart)
    request.session['cart'] = cart
    return redirect('menu')


def adjust_cart(request, product_id):

    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):

    return HttpResponse(status=200)
