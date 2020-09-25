from django.shortcuts import render, redirect
from .models import Product, Topping, ToppingAmount
from pizza_dojo.utils.decorators import select_store_decorator


@select_store_decorator
def menu(request):
    pizza_list = []
    side_list = []
    dessert_list = []
    drink_list = []
    all_products = Product.objects.order_by('position')
    print('ordered products: ', all_products)
    for product in all_products:
        menu_item = {
            'product': None,
            'sizes': [],
        }
        if product.product_type == 'PIZZA':
            pizza_item = [product]
            pizza_toppings = []
            print('Pizza: ', product.sku)
            for top_amt in product.topping_amounts.all():
                pizza_toppings.append(
                    (top_amt.topping.name, top_amt.get_amount_display()))
            pizza_item.append(pizza_toppings)
            pizza_list.append(pizza_item)

        if product.product_type == 'SIDE':
            sizes = []
            if product.small_price:
                sizes.append({'price': str(product.small_price),
                              'size': 'Small'})
            if product.regular_price:
                sizes.append({'price': str(product.regular_price),
                              'size': 'Regular'})
            if product.large_price:
                sizes.append({'price': str(product.large_price),
                              'size': 'Large'})
            menu_item['product'] = product
            menu_item['sizes'] = sizes
            print('side item test: ', menu_item)
            side_list.append(menu_item)

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
