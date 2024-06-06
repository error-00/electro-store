from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("cart_add/<slug:product_slug>", views.cart_add, name="cart_add"),
    path("cart_change/", views.cart_change, name="cart_change"),
    path("cart_remove/", views.cart_remove, name="cart_remove"),
]
