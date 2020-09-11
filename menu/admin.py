from django.contrib import admin
from .models import Product, Topping, ToppingAmount


# Register your models here.
admin.site.register(Product)
admin.site.register(Topping)
admin.site.register(ToppingAmount)
