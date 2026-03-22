from rest_framework import serializers
from .models import Cart, CartItem
from accounts.serializers import UserSerializer


class CartItemInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["product", "quantity"]


class CartItemOutputSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "product", "product_name", "quantity"]


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["quantity"]


class CartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    cart_items = CartItemOutputSerializer(many=True, read_only=True, source="items")

    class Meta:
        model = Cart
        fields = ["id", "user", "cart_items"]
