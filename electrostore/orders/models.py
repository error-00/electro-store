from django.db import models
from users.models import User
from main.models import Product


class OrderitemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True
    )
    created_timestamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    requires_delivery = models.BooleanField(default=False)
    delivery_address = models.TextField(null=True, blank=True)
    payment_on_get = models.BooleanField(default=False)
    order_notes = models.TextField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="In processing")

    class Meta:
        db_table = "order"

    def __str__(self) -> str:
        return f"Order № {self.pk} | User {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(
        to=Product, on_delete=models.SET_DEFAULT, null=True, default=None
    )
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_item"

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.price * self.quantity, 2)

    def __str__(self) -> str:
        return f"Product {self.name} | Order № {self.order.pk}"
