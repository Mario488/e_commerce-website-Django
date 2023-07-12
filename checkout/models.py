from django.db import models


class Order(models.Model):
    email = models.CharField(max_length=50, default="")
    ORDER_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
    ]
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES)
    cost = models.FloatField()


class OrderedProduct(models.Model):
    username = models.CharField(max_length=40, default="")
    product = models.CharField(max_length=40, default="")
    quantity = models.IntegerField()
