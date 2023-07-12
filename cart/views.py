from django.shortcuts import render, redirect
from . models import Cart as cart_product
from django.contrib import messages
from home import models


def Cart(request):
    curr_user = None
    email = None
    if request.user.is_authenticated:
        curr_user = request.user
        email = curr_user.email
    if request.method == 'POST' and request.POST['delete'] == 'delete':
        phone = request.POST['phone']
        phones = cart_product.objects.filter(Email=email, Product_name=phone)
        phones.delete()
        products = cart_product.objects.filter(Email=email)
        product_names = [pr.Product_name for pr in products]
        phones = models.Smartphones.objects.filter(
            Series__in=product_names)
        phones_info = zip(phones, products)
        return render(request, 'cart.html', {'phones': phones_info})
    if request.method == 'POST' and request.POST['delete'] == 'delete1':
        if request.user.is_authenticated:
            product = request.POST['product']
            exist = cart_product.objects.filter(
                Email=email, Product_name=product)
            if not (exist.exists()):
                quantity = request.POST['quantity']
                add_product = cart_product(
                    Email=email, Product_name=product, Quantity=quantity)
                add_product.save()
                messages.success(request, 'Item Added To Cart')
                return redirect('smartphones')
            else:
                messages.success(request, 'Item Already Added')
                return redirect('smartphones')
        else:
            messages.success(request, 'Please Login')
            return redirect('login')

    if request.method == 'GET':
        products = cart_product.objects.filter(Email=email)
        product_names = [pr.Product_name for pr in products]
        phones = models.Smartphones.objects.filter(
            Series__in=product_names)
        phones_info = zip(phones, products)
        return render(request, 'cart.html', {'phones': phones_info})
