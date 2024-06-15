from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import Cart
from orders.forms import CreateOrderForm
from .models import Order, OrderItem


def create_order(request):
    if request.method == "POST":
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # create order
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                            email=form.cleaned_data["email"],
                            requires_delivery=form.cleaned_data["requires_delivery"],
                            delivery_address=form.cleaned_data["delivery_address"],
                            payment_on_get=form.cleaned_data["payment_on_get"],
                            order_notes=form.cleaned_data["order_notes"],
                        )

                        # create ordered goods
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(
                                    f"Not enough product {name} quantity\
                                                    In stock - {product.quantity}"
                                )

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # empty users cart after creating and order
                        cart_items.delete()
                        print("Order is created!")
                        return redirect("users:profile")
            except ValidationError as e:
                print(e)
                return redirect("cart:order")

    else:
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {"title": "Create order", "form": form}

    return render(request, "orders/create_order.html", context=context)
