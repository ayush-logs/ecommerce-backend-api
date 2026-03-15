from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Product, Category
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CategorySerializer,
)


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().filter(is_active=True)
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        else:
            return ProductDetailSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
