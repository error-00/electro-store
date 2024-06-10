from django.http import JsonResponse
from django.shortcuts import redirect
from main.models import Product
from .models import Cart


def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    try:
        quantity = int(request.POST.get("quantity", 1))
        if quantity < 1:
            quantity = 1
    except ValueError:
        quantity = 1

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += quantity
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product
        )

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += quantity
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=quantity
            )

    if not request.session.session_key:
        request.session.create()

    return redirect(request.META["HTTP_REFERER"])


def cart_change(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    quantity = int(request.POST.get("quantity"))
    if quantity > 0 and cart.quantity != quantity:
        cart.quantity = quantity
        cart.save()

    return redirect(request.META["HTTP_REFERER"])


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META["HTTP_REFERER"])
