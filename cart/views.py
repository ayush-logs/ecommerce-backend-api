from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .models import CartItem, Cart
from .serializers import CartSerializer, CartItemSerializer


class CartCreateView(CreateAPIView):
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
