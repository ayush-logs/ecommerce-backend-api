from rest_framework.viewsets import ModelViewSet
from .models import CartItem, Cart
from .serializers import CartSerializer, CartItemSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
