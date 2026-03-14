from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  # ask: expose all fields or explicitly list them?

        # optional decisions:
        # read_only_fields = []  # e.g. id, created_at, updated_at
        # extra_kwargs = {}  # add validation or field options if needed


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"  # ask: expose all fields or explicitly list them?

        # optional decisions:
        # read_only_fields = []  # e.g. id, created_at, updated_at
        # extra_kwargs = {}  # add validation or field options if needed
