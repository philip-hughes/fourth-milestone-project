import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from menu.models import Product
from select_store.models import Store


class Order(models.Model):

    STATUS_CHOICES = (
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In progress'),
        ('DONE', 'Done'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    order_status = models.CharField(choices=STATUS_CHOICES, default='NEW', max_length=20, null=True, blank=True)
    store = models.ForeignKey(Store, null=False, blank=False, on_delete=models.CASCADE)
    delivery = models.BooleanField(default=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=True, blank=True,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    size = models.CharField(max_length=20, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False, editable=False, default=0)
    customizations = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'