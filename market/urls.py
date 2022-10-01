
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('shop',views.shop,name="shop"),
    path('login', views.login,name="login"),
    path('logout', views.logout,name="logout"),
    path('register', views.register,name="register"),
    path('product/<int:id>', views.product,name="product"),
    path('cart', views.cart,name="cart"),
    path('addto_wishlist/<int:id>', views.addto_wishlist,name="wish_list"),
    path('dashboard', views.dashboard,name="dshboard"),
    path('orders', views.orders,name="orders"),
    path('checkout', views.checkout,name="checkout"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('addtocart/<int:id>', views.addtocart,name="addtocart"),
    path('wishlist', views.wishlist,name="wishlist"),
    path('removewish/<int:id>', views.removewish,name="removewish"),
    path('removecart/<int:id>', views.removecart,name="removecart"),


]