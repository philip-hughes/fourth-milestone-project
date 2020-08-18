from django.shortcuts import (render, redirect, reverse, HttpResponse)


def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    return redirect('menu')


def adjust_cart(request, item_id):

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):

    return HttpResponse(status=200)
