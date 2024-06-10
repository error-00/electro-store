from django.contrib import admin
from .models import Category, Product, ProductImage, Rating, Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Rating)
admin.site.register(Review)
