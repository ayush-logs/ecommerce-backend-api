from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Order
from orders.serializers import OrderListSerializer
from .serializers import OrderDetailSerializer
from .services import create_order_from_cart


class OrderListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=self.request.user)
        return Response(OrderListSerializer(orders, many=True).data)

    def post(self, request, *args, **kwargs):
        order = create_order_from_cart(user=request.user)
        return Response(
            OrderDetailSerializer(order).data, status=status.HTTP_201_CREATED
        )


class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related(
            "order_items__product"
        )
