from django.shortcuts import (render, redirect, reverse, HttpResponse)


def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    print('Cart before add: ', request.session.get('cart', []))
    print('Adding to cart...')
    size = request.POST.get('size')
    cart = request.session.get('cart', [])
    quantity = request.POST.get('quantity')
    cart.append({'product_id': product_id, 'size': size})
    print('Added to cart: ', cart)
    request.session['cart'] = cart
    return redirect('menu')


def adjust_cart(request, product_id):

    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):

    return HttpResponse(status=200)
