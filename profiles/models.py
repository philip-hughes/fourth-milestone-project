from django.db import models
from django.contrib.auth.models import User


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    default_address = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
