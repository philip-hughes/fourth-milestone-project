

def cart_contents(request):

    cart = request.session.get('cart', {})
    if cart != {}:
        product_name = cart['product_name']
        print('Product name:', product_name)
        context = {
            'product_name': product_name,
        }
    else:
        context = {}
    print('context:', context)
    return context
