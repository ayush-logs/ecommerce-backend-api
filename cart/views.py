from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import CartItem, Cart
from .serializers import (
    CartSerializer,
    CartItemCreateSerializer,
    CartItemUpdateSerializer,
)
from rest_framework.response import Response


class CartItemAddView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CartItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data["product"]
        quantity = serializer.validated_data["quantity"]

        cart, _ = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={"quantity": quantity},
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response({"message": "Item added to cart"})


class CartRetrieveView(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


# PATCH  /cart/items/{id}/  → update quantity
class CartItemUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemUpdateSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)


class CartItemDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
