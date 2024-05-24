from django.urls import path
from . import views

app_name = "goods"

urlpatterns = [
    path("<slug:product_slug>/", views.product, name="product"),
]
