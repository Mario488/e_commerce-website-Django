from django.contrib import admin
from django.urls import path
from home import views as home_views
from smartphones import views as smartphone_views
from user_auth import views as auth_views
from cart import views as cart
from favorites import views as favorite
from checkout import views as checkout
from django.conf import settings
from django.conf.urls.static import static
from reviews import views as reviews
from contacts import views as contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name="home"),
    path('smartphones', smartphone_views.smartphones, name='smartphones'),
    path('logout/', auth_views.logout, name='logout'),
    path('login/', auth_views.login, name='login'),
    path('sign_up/', auth_views.sign_up, name='sign_up'),
    path('password/', auth_views.passwordChange, name='change_password'),
    path('profile/', auth_views.profile, name="profile"),
    path('cart', cart.Cart, name="cart"),
    path('favorite/', favorite.favorites, name="favorites"),
    path('checkout/', checkout.checkout, name="checkout"),
    path('review/', reviews.review, name="review"),
    path('contacts', contact_us.Contact_Us, name="contacts"),
]
