from .views import (
    CartRetrieveView,
    CartItemAddView,
    CartItemUpdateView,
    CartItemDeleteView,
)
from django.urls import path

# POST   /cart/items/       → add item
# GET    /cart/             → get current cart
# PATCH  /cart/items/{id}/  → update quantity
# DELETE /cart/items/{id}/  → remove item


urlpatterns = [
    path("cart/items/", CartItemAddView.as_view(), name="createj"),
    path("cart/", CartRetrieveView.as_view(), name="get_cart"),
    path("cart/items/<int:pk>", CartItemUpdateView.as_view(), name="update_item"),
    path("cart/items/<int:pk>", CartItemDeleteView.as_view(), name="delete_item"),
]
