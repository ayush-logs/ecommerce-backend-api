from django.db import transaction
from django.core.exceptions import ValidationError

from cart.models import Cart, CartItem
from orders.models import Order, OrderItem
from products.models import Product
from django.db.models import F


def create_order_from_cart(user):
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        raise ValidationError("Cart does not exist")

    cart_items = CartItem.objects.filter(cart=cart).select_related("product")

    if not cart_items.exists():
        raise ValidationError("Cart is empty.")

    with transaction.atomic():
        order = Order.objects.create(user=user)

        order_items = []

        for cart_item in cart_items:
            order_items.append(
                OrderItem(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price,
                )
            )

        OrderItem.objects.bulk_create(order_items)

        # decrement stock atomically
        for item in cart_items:
            Product.objects.filter(id=item.product_id).update(
                stock=F("stock") - item.quantity
            )

        cart.delete()

    return Order.objects.prefetch_related("order_items__product").get(pk=order.id)
