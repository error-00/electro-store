from django.contrib import admin
from .models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestampt"
    search_fields = "product", "quantity", "created_timestampt"
    readonly_fields = ("created_timestampt",)
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "quantity", "created_timestampt"]
    list_filter = ["created_timestampt", "user", "product__name"]
