from django.shortcuts import (render, redirect, reverse, HttpResponse)


def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    print('Item id: ', item_id)
    pizza_name = request.POST.get(item_id)
    cart = request.session.get('cart', {})
    request.session['cart'] = {'product_name': item_id}
    return redirect('menu')


def adjust_cart(request, item_id):

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):

    return HttpResponse(status=200)
