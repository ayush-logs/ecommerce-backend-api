from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Product, Category
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CategorySerializer,
)


class ProductViewSet(ReadOnlyModelViewSet):
    lookup_field = "slug"
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        else:
            return ProductDetailSerializer

    def get_queryset(self):
        return Product.objects.all().filter(is_active=True).select_related("category")


class CategoryViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
