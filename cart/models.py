from django.db import models


class Cart(models.Model):
    Email = models.CharField(max_length=40, default="")
    Product_name = models.CharField(max_length=40, default="")
    Quantity = models.IntegerField(default=1)
