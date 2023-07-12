from django.db import models


class ProductReview(models.Model):
    User = models.CharField(max_length=40, default="")
    Product = models.CharField(max_length=30, default="")
    Review_title = models.CharField(max_length=21, default="")
    Review = models.TextField(max_length=330)
    Stars = models.IntegerField(default=1)
