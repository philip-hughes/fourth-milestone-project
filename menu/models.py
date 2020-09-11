from django.db import models


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = (
        ('PIZZA', 'Pizza'),
        ('SIDE', 'Side'),
        ('DESSERT', 'Dessert'),
        ('DRINK', 'Drink')
    )

    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    product_type = models.CharField(choices=PRODUCT_TYPE_CHOICES, max_length=20, default='PIZZA')
    position =  models.CharField(max_length=10, null=False, blank=False, default=1)
    toppings = models.ManyToManyField('Topping', through='ToppingAmount', related_name='pizzas')
    small_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    regular_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Topping(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ToppingAmount(models.Model):

    REGULAR = 1
    DOUBLE = 2
    TRIPLE = 3
    AMOUNT_CHOICES = (
        (REGULAR, 'Regular'),
        (DOUBLE, 'Double'),
        (TRIPLE, 'Triple'),
    )

    pizza = models.ForeignKey('Product', related_name='topping_amounts', on_delete=models.SET_NULL, null=True)
    topping = models.ForeignKey('Topping', related_name='topping_amounts', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)
 