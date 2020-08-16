from django.shortcuts import render
from .models import Pizza, Topping, ToppingAmount

def menu(request):
    pizza_list = []
    for pizza in Pizza.objects.all():
        pizza_item = [pizza]
        pizza_toppings = []
        print('Pizza: ', pizza.name)
        for top_amt in pizza.topping_amounts.all():
            pizza_toppings.append((top_amt.topping.name, top_amt.get_amount_display()))
        pizza_item.append(pizza_toppings)    
        pizza_list.append(pizza_item)
    context = {
        'pizzas': pizza_list
    }       
    return render(request, 'menu/menu.html', context)