from django.db import models

class Favorite(models.Model):
    Email = models.CharField(max_length=40, default="")
    Product_name = models.CharField(max_length=40, default="")
