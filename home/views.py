from django.shortcuts import render
from . models import Smartphones
from checkout import models as orders


def home(request):
    most_ordered = orders.OrderedProduct.objects.all()
    most3Ordered = {}
    for pr in most_ordered:
        if pr.product not in most3Ordered:
            most3Ordered[pr.product] = pr.quantity
        else:
            most3Ordered[pr.product] += pr.quantity

    phones = dict(
        sorted(most3Ordered.items(), key=lambda x: x[1], reverse=True))
    top3 = []
    count = 0
    for phone in phones:
        if count == 3:
            break
        else:
            top3.append(phone)
            count += 1
    top3phones = Smartphones.objects.filter(Series__in=top3)
    return render(request, 'home.html', {'phones': top3phones})
