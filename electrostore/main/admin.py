from django.contrib import admin
from .models import Category, Product, ProductImage, Rating, Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount"]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["product", "user", "value"]
    search_fields = ["product", "user"]
    list_filter = ["product", "value", "user"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "body", "rating"]
    search_fields = ["user", "product", "body"]

