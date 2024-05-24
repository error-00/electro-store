from django.shortcuts import render
from .models import Category, Product
from django.db.models import Avg
import random


def index(request):
    categories = Category.objects.all()
    
    rand_cats = list(Category.objects.all())
    random.shuffle(rand_cats)
    rand_cats = rand_cats[:3]

    products = Product.objects.all().annotate(average_rating=Avg("ratings__value"))

    context = {
        "title": "Electro - HTML Ecommerce Template",
        "categories": categories,
        "random_cats": rand_cats,
        "products": products.order_by('-id')[:16],
        "top_sellings": products.order_by("-average_rating")[:8],
    }
    return render(request, "main/index.html", context)
