from django.shortcuts import render, redirect
from . import models
from home import models as smartphones
from django.contrib import messages
import json
from cart import models as user_cart


def checkout(request):
    if request.method == 'POST':
        purchasedPR = request.POST['purchasedPR']
        PRquantity = request.POST['PRquantity']
        PRprice = request.POST['PRprice']
        purchasedPR_list = purchasedPR.split(',')
        PRquantity_list = PRquantity.split(',')
        PRprice_list = PRprice.split(',')
        context = list(zip(purchasedPR_list, PRquantity_list, PRprice_list))
        context_json = json.dumps(context)
        return render(request, 'checkout.html', {'context': context, 'context_json': context_json})
    if request.method == 'GET':

        Email = request.user.email
        Cart = user_cart.Cart.objects.filter(Email=Email)
        Cart.delete()
        context = request.GET.get('info')
        info = json.loads(context)
        total_cost = request.GET.get('total_cost')
        Username = request.user.username
        order = models.Order(email=Email, status='P', cost=total_cost)
        order.save()
        for a, b, c in info:
            orderedProduct = models.OrderedProduct(
                username=Username, product=a, quantity=b)
            orderedProduct.save()
            Smartphones = smartphones.Smartphones.objects.get(Series=a)
            Smartphones.Quantity -= int(b)
            Smartphones.save()
        messages.success(
            request, 'Thank you for your purchase! Your order has been processed and will be shipped shortly.')
        return redirect('home')
