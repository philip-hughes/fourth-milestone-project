from django.shortcuts import (render, redirect, reverse, HttpResponse)


def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    print('Item id: ', product_id)
    pizza_name = request.POST.get(product_id)
    cart = request.session.get('cart', [])
    request.session['cart'].append({'product_id': product_id})
    return redirect('menu')


def adjust_cart(request, product_id):

    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):

    return HttpResponse(status=200)
