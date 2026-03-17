from rest_framework.routers import SimpleRouter
from .views import CartCreateView, CartItemViewSet
from django.urls import path, include

router = SimpleRouter()
router.register(r"cartitems", CartItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('carts/', CartCreateView.as_view(), name='create'),
]
