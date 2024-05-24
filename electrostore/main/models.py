from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category_images')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    little_description = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.name

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price

    def display_id(self):
        return f"{self.id:05}"

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings:
            rating = int(sum(rating.value for rating in ratings) / ratings.count())
            print(rating)
            return rating
        return 0


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return f"Image for {self.product.name}"


class Rating(models.Model):
    product = models.ForeignKey(
        Product, related_name="ratings", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="ratings", on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("product", "user")  # one user one mark

    def __str__(self):
        return f"{self.value} stars for {self.product.name} by {self.user}"
