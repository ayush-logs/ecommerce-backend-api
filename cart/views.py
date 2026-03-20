from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView
from .models import CartItem, Cart
from .serializers import (
    CartSerializer,
    CartItemInputSerializer,
    CartItemUpdateSerializer,
    CartItemOutputSerializer,
)
from rest_framework.response import Response

from .services import add_item_to_cart


class CartRetrieveView(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


# noinspection PyMethodMayBeStatic
class CartItemAddView(APIView):
    def post(self, request):

        serializer = CartItemInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart_item = add_item_to_cart(
            user=request.user,
            product=serializer.validated_data["product"],
            quantity=serializer.validated_data["quantity"],
        )

        return Response(
            CartItemOutputSerializer(cart_item).data, status=status.HTTP_201_CREATED
        )


class CartItemUpdateView(UpdateAPIView):
    serializer_class = CartItemUpdateSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)


class CartItemDeleteView(DestroyAPIView):
    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
