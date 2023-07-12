from django.shortcuts import render, redirect
from . import models
from home import models as phone
from django.contrib import messages
from django.urls import reverse


def review(request):
    if request.method == 'POST':
        name = request.user.username
        review_title = request.POST['review-title']
        review = request.POST['review']
        product = request.POST['product_Name']
        stars = request.POST['stars']
        New_Review = models.ProductReview(
            User=name, Product=product, Review_title=review_title, Review=review, Stars=stars)
        New_Review.save()
        messages.success(request, 'Thank you for your review!')
    return redirect(reverse('smartphones'))
