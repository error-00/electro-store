from django.shortcuts import render
from main.models import Product, Category
from django.db.models import Avg, F, ExpressionWrapper, DecimalField
from django.core.paginator import Paginator
from goods.utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    query = request.GET.get("q", None)
    sort_option = request.GET.get("sort", None)

    if category_slug == "all":
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Product.objects.filter(category__slug=category_slug)

    if sort_option == "0":  # Popular
        goods = goods.annotate(average_rating=Avg("ratings__value")).order_by(
            "-average_rating"
        )
    elif sort_option == "1":  # Price: Low to High
        goods = goods.annotate(
            sell_price=ExpressionWrapper(
                F("price") - F("price") * F("discount") / 100,
                output_field=DecimalField(max_digits=7, decimal_places=2),
            )
        ).order_by("sell_price")
    elif sort_option == "2":  # Price: High to Low
        goods = goods.annotate(
            sell_price=ExpressionWrapper(
                F("price") - F("price") * F("discount") / 100,
                output_field=DecimalField(max_digits=7, decimal_places=2),
            )
        ).order_by("-sell_price")
    elif sort_option == "3":  # Discount
        goods = goods.filter(discount__gt=0)

    categories = Category.objects.all()
    top_sellings = (
        Product.objects.all()
        .annotate(average_rating=Avg("ratings__value"))
        .order_by("-average_rating")[:3]
    )
    total_count = Product.objects.count()

    paginator = Paginator(goods, 6)
    current_page = paginator.page(int(page))

    context = {
        "title": "Catalog",
        "goods": current_page,
        "categories": categories,
        "top_sellings": top_sellings,
        "total_count": total_count,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    related_products = Product.objects.filter(category=product.category)

    context = {
        "title": product.name,
        "product": product,
        "categories": categories,
        "related_products": related_products,
    }

    return render(request, "goods/product.html", context)
