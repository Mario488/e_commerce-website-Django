from django.shortcuts import render
from . import models
from django.http import JsonResponse
from home import models as phone
from cart import models as cart
from home import models as sm_phone


def favorites(request):
    email = request.user.email
    if request.method == 'GET':
        favorites = models.Favorite.objects.filter(Email=email)
        if favorites.exists():
            phones = [pr.Product_name for pr in favorites]
            smartphones = phone.Smartphones.objects.filter(Series__in=phones)
            return render(request, 'favorites.html', {'smartphones': smartphones})
        else:
            return render(request, 'favorites.html')
    if request.method == 'POST':
        if request.POST.get('removed') == 'Item Already Added':
            smphone = request.POST.get('phone')
            added = request.POST.get('added')
            removed = request.POST.get('removed')
            outOfStock = request.POST.get('outOfStock')
            exist = cart.Cart.objects.filter(Email=email, Product_name=smphone)
            if exist.exists():
                return JsonResponse({'removed': removed})
            else:
                check_Quantity = sm_phone.Smartphones.objects.get(
                    Series=smphone)
                if check_Quantity.Quantity > 0:
                    new_p = cart.Cart(
                        Email=email, Product_name=smphone, Quantity=1)
                    new_p.save()
                    return JsonResponse({'added': added})
                else:
                    return JsonResponse({'outOfStock': outOfStock})
        if request.POST.get('removed') == 'Item Removed':
            smphone = request.POST.get('phone')
            removed = request.POST.get('removed')
            remove_item = models.Favorite.objects.get(
                Email=email, Product_name=smphone)
            remove_item.delete()
            return JsonResponse({'removed': removed})
        if request.POST.get('removed') == 'False' or request.POST.get('removed') == 'Item Removed From Favorites':
            item_id = request.POST.get('itemId')
            added = request.POST.get('added')
            removed = request.POST.get('removed')
            if removed == 'False':
                new_favorite = models.Favorite(
                    Email=email, Product_name=item_id)
                new_favorite.save()
                return JsonResponse({'added': added})
            else:
                del_favorite = models.Favorite.objects.filter(
                    Email=email, Product_name=item_id)
                del_favorite.delete()
                return JsonResponse({'removed': removed})
