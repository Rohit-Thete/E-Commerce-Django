from .models import *
from django.db import transaction
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404


def create_order(user, items):
    total = 0

    with transaction.atomic():
        order = Order.objects.create(user=user, total_bill=0)

        for item in items:
            product = Product.objects.select_for_update().get(id=item["product"].id)
            quantity = item["quantity"]
            price = product.price

            # TODO: use select for update to lock the product row to prevent race conditions
            # TODO: How client know which item out of stock?
            if product.stock < quantity:
                raise ValidationError(
                    {
                        "error": f"available stock for {product.name} is less than required Quantity"
                    }
                )

            obj = OrderItem.objects.create(
                order=order, product=product, quantity=quantity, price=price
            )
            # TODO: use item_subtotal
            total += obj.item_subtotal

            order.total_bill = total
            # TODO: only update total_bill field
            order.save(update_fields=["total_bill"])

            product.stock -= quantity
            # TODO: only update stock field
            product.save(update_fields=["stock"])

    return order


def create_cart(user, items):
    total = 0
    with transaction.atomic():
        cart, _ = Cart.objects.get_or_create(user=user, defaults={"cart_total": 0})

        for item in items:
            product = Product.objects.select_for_update().get(id=item["product"].id)
            quantity = item["quantity"]
            price = product.price

            if product.stock < quantity:
                raise ValidationError(
                    {
                        "error": f"available stock for {product.name} is less than required Quantity"
                    }
                )

            obj = CartItem.objects.create(cart=cart, product=product, quantity=quantity)
            total += obj.quantity * product.price
            cart.cart_total = total
            cart.save(update_fields=["cart_total"])

    return cart


def checkout_cart(user):
    with transaction.atomic():
        cart = Cart.objects.prefetch_related("items__product").get(user=user)

        if not cart.items.exists():
            raise ValidationError("cart is empty")

        formatted_items = [

        {
            "product": item.product,
            "quantity": item.quantity,
        }

        for item in cart.items.all()
        ]

        for item in cart.items.all():
            product = Product.objects.select_for_update().get(pk=item.product.pk)

            if item.quantity > product.stock:
                raise ValidationError(
                    {
                        "error": f"available stock for {product.name} is less than required Quantity"
                    }
                )

        order = create_order(user=user, items = formatted_items)

        cart.items.all().delete()

        return order


def update_cart_item(user,quantity,pk):

    cart_item= get_object_or_404(CartItem.objects.select_related("product"),pk=pk,cart__user=user)

    if quantity > cart_item.product.stock:
        raise ValidationError({"msg":f"only {cart_item.product.stock} units available"})
    
    if quantity == 0:
        cart_item.delete()

        return None
    
    cart_item.quantity=quantity
    cart_item.save(update_fields=["quantity"])

    return cart_item
