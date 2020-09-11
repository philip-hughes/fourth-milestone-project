from django.shortcuts import render, redirect
from .models import Product, Topping, ToppingAmount


def menu(request):
    pizza_list = []
    side_list = []
    dessert_list = []
    drink_list = []
    all_products = Product.objects.order_by('position')
    print('ordered products: ', all_products)
    for product in all_products:
        if product.product_type == 'PIZZA':
            pizza_item = [product]
            pizza_toppings = []
            print('Pizza: ', product.sku)
            for top_amt in product.topping_amounts.all():
                pizza_toppings.append((top_amt.topping.name, top_amt.get_amount_display()))
            pizza_item.append(pizza_toppings)
            pizza_list.append(pizza_item)

        if product.product_type == 'SIDE':
            side_list.append(product)
        if product.product_type == 'DESSERT':
            dessert_list.append(product)
        else:
            drink_list.append(product)
    print('sides list: ', side_list)
    
    context = {
        'pizzas': pizza_list,
        'sides': side_list,
        'desserts': dessert_list,
        'drinks': drink_list,
    }
    return render(request, 'menu/menu.html', context)


def flush_session(request):
    request.session.flush()
    return redirect('menu')
