from django.shortcuts import render


def checkout(request):
    context = {
        'stripe_public_key': 'pk_test_51HKvzZBCwxzuCpWqiPY8CFQSS7AGDCyu80hHnvzJDF9yFnCxsZdBMDJLeGRrDDME5ShnbuW5CnoPx9547njRbCl300fLtf06W6',
        'client_secret': 'client secret test',
    }
    return render(request, 'checkout/checkout.html', context)
