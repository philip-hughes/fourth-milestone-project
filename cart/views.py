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
    customizations = request.POST.get('customizations')
    if product_type == 'PIZZA':
        cart.extend([{'product_id': product_id, 'size': size, 'item_price': price, 'quantity': 1, 'customizations': customizations}] * quantity)
        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER'))

    if cart == []:
        cart.append({'product_id': product_id, 'size': size, 'item_price': price, 'quantity': quantity, 'customizations': customizations})
        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER'))
    else:    
        for index, item in enumerate(cart):
            if (item['product_id'] == product_id) and (item['size'] == size):
                cart[index]['quantity'] += quantity
                request.session['cart'] = cart
                return redirect(request.META.get('HTTP_REFERER'))
    """ Cart has items, but none are identical to the new item """
    cart.append({'product_id': product_id, 'size': size, 'item_price': price, 'quantity': quantity, 'customizations': customizations})
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER'))


def adjust_cart(request, product_id):
    cart = request.session.get('cart', [])
    adjust_type = request.POST.get('adjust-type')
    item_index = int(request.POST.get('item-index'))   
    if adjust_type == 'remove':
        print('adjust type: ', adjust_type)
        cart.pop(item_index)
        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    print('adjust type: ', adjust_type )
 
    print('adjusting product: ', cart[item_index])

    return redirect(reverse('view_cart'))

