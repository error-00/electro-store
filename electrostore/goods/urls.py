from django.urls import path
from . import views

app_name = "goods"

urlpatterns = [
    path("search", views.catalog, name="search"),
    path("<slug:product_slug>/", views.product, name="product"),
    path("catalog/<slug:category_slug>/", views.catalog, name="catalog"),
]
