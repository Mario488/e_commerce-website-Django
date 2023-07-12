from django.shortcuts import render
from home import models
from favorites import models as fav
from reviews import models as review


def smartphones(request):
    if request.method == 'POST':
        phone_to_search = request.POST['search_input']
        if phone_to_search != '':
            smartphones = models.Smartphones.objects.filter(
                Series__contains=phone_to_search)
            return render(request, 'Smartphones.html', {'smartphones': smartphones})
    if request.method == 'GET':
        product = request.GET.get('product')
        if product != None:
            smartphone = models.Smartphones.objects.filter(
                Series__contains=product)
            interfaces = []
            options = []
            for prod in smartphone:
                interfaces.extend(prod.Interfaces.split(','))
                break
            for prod in smartphone:
                options.extend(prod.Options.split(','))

            context = {'product': smartphone,
                       'interfaces': interfaces, 'options': options}

            check_reviews = review.ProductReview.objects.filter(
                Product=product)

            return render(request, 'Product.html', {'context': context, 'reviews': check_reviews})

    smartphones = models.Smartphones.objects.all()
    if request.user.is_authenticated:
        email = request.user.email
        favorites = fav.Favorite.objects.filter(Email=email)
        favorites_list = [fav.Product_name for fav in favorites]
        return render(request, 'Smartphones.html', {'smartphones': smartphones, 'favorites': favorites_list})
    return render(request, 'Smartphones.html', {'smartphones': smartphones})
