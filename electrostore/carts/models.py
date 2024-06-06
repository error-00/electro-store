from django.db import models

from users.models import User
from main.models import Product


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestampt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cart"

    objects = CartQuerySet().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity)

    def __str__(self):
        if self.user:
            return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"
        return f"Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}"
