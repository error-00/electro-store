from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("goods/", include("goods.urls", namespace="goods")),
    path("users/", include("users.urls", namespace="users")),
    path("cart/", include("carts.urls", namespace="cart")),
    path("orders/", include("orders.urls", namespace="orders")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
