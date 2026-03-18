from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from products.models import Product

User = get_user_model()


class Status(models.TextChoices):
    PENDING = "PR", "Pending"
    PAID = "PD", "Paid"
    SHIPPED = "SP", "Shipped"
    DELIVERED = "DV", "Delivered"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.PENDING
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"
        constraints = [
            models.UniqueConstraint(
                fields=["order", "product"], name="unique_order_item"
            )
        ]
