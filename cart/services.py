from django.db import transaction
from cart.models import Cart, CartItem


def add_item_to_cart(user, product, quantity):
    with transaction.atomic():
        cart, _ = Cart.objects.get_or_create(user=user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={"quantity": quantity},
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return cart_item
