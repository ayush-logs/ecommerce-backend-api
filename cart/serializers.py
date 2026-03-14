from rest_framework import serializers
from .models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"  # ask: expose all fields or explicitly list them?

        # optional decisions:
        # read_only_fields = []  # e.g. id, created_at, updated_at
        # extra_kwargs = {}  # add validation or field options if needed


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"  # ask: expose all fields or explicitly list them?

        # optional decisions:
        # read_only_fields = []  # e.g. id, created_at, updated_at
        # extra_kwargs = {}  # add validation or field options if needed
