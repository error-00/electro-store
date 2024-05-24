from django.shortcuts import render
from main.models import Product, Category

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    related_products = Product.objects.filter(category=product.category)

    context = {
        'title': product.name,
        'product': product,
        'categories': categories,
        'related_products': related_products,
    }

    return render(request, 'goods/product.html', context)