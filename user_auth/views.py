from django.shortcuts import render, redirect, HttpResponse
from e_commerce.settings import BASE_DIR
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_method
from django.contrib.auth import login as login_method
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from checkout import models as order_info
from favorites import models as favorite
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from cart import models as cart_pr
from reviews import models as model_reviews


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.info(self.request, 'Password Changed Successfully!')
        return super().form_valid(form)


def passwordChange(request):
    return MyPasswordChangeView.as_view()(request)


def profile(request):
    username = request.user.username
    email = request.user.email
    reg_orders = order_info.Order.objects.filter(email=email)

    favorites = favorite.Favorite.objects.filter(Email=email)

    reviews = model_reviews.ProductReview.objects.filter(User=username)
    reviews_count = reviews.count()

    if request.method == 'POST' and request.POST['method'] == 'post1':
        image = request.FILES['image']
        new_filename = f"{username}.{image.name.split('.')[-1]}"
        fs = FileSystemStorage()
        if fs.exists(new_filename):
            fs.delete(new_filename)
        fs.save(new_filename, image)
        return render(request, 'profile.html',
                      {'username': username,
                       'email': email,
                       'reg_orders': reg_orders,
                       'favorites': favorites,
                       'reviews': reviews,
                       'reg_orders_count': reg_orders.count(),
                       'favorites_count': favorites.count()})
    if request.method == 'POST' and request.POST['method'] == 'post_username':
        new_username = request.POST['username']
        users = User.objects.all()

        users_list = [user.username for user in users]

        if new_username in users_list:
            messages.error(request, 'Username Already Exists. Try another.')
            return render(request, 'profile.html',
                          {'username': username,
                           'email': email,
                           'reg_orders': reg_orders,
                           'favorites': favorites,
                           'reviews': reviews,
                           'reg_orders_count': reg_orders.count(),
                           'favorites_count': favorites.count()})
        else:
            currentUser = User.objects.get(username=username)
            currentUser.username = new_username
            currentUser.save()

            media_root = os.path.join(BASE_DIR, 'pfp_images')
            old_name = f'{username}.jpg'
            new_name = f'{new_username}.jpg'

            old_file_path = os.path.join(media_root, old_name)
            new_file_path = os.path.join(media_root, new_name)

            os.rename(old_file_path, new_file_path)

            Ordered_Products = order_info.OrderedProduct.objects.filter(
                username=username)
            for op in Ordered_Products:
                op.username = new_username
                op.save()
            messages.success(request, 'Username Changed Successfully!')
            return render(request, 'profile.html',
                          {'username': username,
                           'email': email,
                           'reg_orders': reg_orders,
                           'favorites': favorites,
                           'reviews': reviews,
                           'reg_orders_count': reg_orders.count(),
                           'favorites_count': favorites.count()})
    if request.method == 'POST' and request.POST['method'] == 'post_email':
        new_email = request.POST['email']
        users = User.objects.all()
        users_list = [us.email for us in users]

        if new_email in users_list:
            messages.error(request, 'Email Already Exists. Try another')
            return render(request, 'profile.html',
                          {'username': username,
                           'email': email,
                           'reg_orders': reg_orders,
                           'favorites': favorites,
                           'reviews': reviews,
                           'reg_orders_count': reg_orders.count(),
                           'favorites_count': favorites.count()})
        else:
            user = User.objects.get(email=email)
            user.email = new_email
            user.save()
            orders = order_info.Order.objects.filter(email=email)
            for order in orders:
                order.email = new_email
                order.save()
            favorites = favorite.Favorite.objects.filter(Email=email)
            for fav in favorites:
                fav.Email = new_email
                fav.save()
            cart_products = cart_pr.Cart.objects.filter(Email=email)
            for cp in cart_products:
                cp.Email = new_email
                cp.save()
            messages.success(request, 'Email Changed Successfully!')
            return render(request, 'profile.html',
                          {'username': username,
                           'email': email,
                           'reg_orders': reg_orders,
                           'favorites': favorites,
                           'reviews': reviews,
                           'reg_orders_count': reg_orders.count(),
                           'favorites_count': favorites.count()})
    if request.method == 'POST' and request.POST['method'] == 'post_password':
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            user = User.objects.get(username=username)
            user.set_password(password1)
            user.save()
            messages.success(request, 'Password Changed Successfully!')
            return render(request, 'profile.html',
                          {'username': username,
                           'email': email,
                           'reg_orders': reg_orders,
                           'favorites': favorites,
                           'reviews': reviews,
                           'reg_orders_count': reg_orders.count(),
                           'favorites_count': favorites.count()})
        else:
            messages.error(request, "Password fields didn't match")
            return render(request, 'profile.html',

                          {'username': username,
                           'email': email,
                           'reg_orders': reg_orders,
                           'favorites': favorites,
                           'reviews': reviews,
                           'reg_orders_count': reg_orders.count(),
                           'favorites_count': favorites.count()})

    return render(request, 'profile.html',
                  {'username': username,
                   'email': email,
                   'reg_orders': reg_orders,
                   'favorites': favorites,
                   'reviews': reviews,
                   'reviews_count': reviews_count,
                   'reg_orders_count': reg_orders.count(),
                   'favorites_count': favorites.count()})


def logout(request):
    print('Logout view called')
    logout_method(request)
    messages.success(request, 'You\'ve been logged out')
    return redirect('login')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_method(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('home')
        else:
            return render(request, 'login.html', {'message': 'Invalid username or password!'})
    return render(request, 'login.html', {'message': ''})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(
                request, "Password restrictions must match! Try again.")
            form = RegisterForm()
            return render(request, 'sign_up.html', {'form': form})
        messages.success(request, "Account, Successfully Created!")
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'sign_up.html', {'form': form})
