from .models import *
from django.db import transaction
from rest_framework.exceptions import ValidationError


def create_order(user,items):
    total = 0

    with transaction.atomic():
        order = Order.objects.create(user = user,total_bill = 0)

        for item in items:
            product = item["product"]
            quantity = item["quantity"]
            price = product.price

            if product.stock < quantity:
                raise ValidationError({"error":"available stock is less than required Quantity"})
            
            obj = OrderItem.objects.create(
                order = order,
                product = product,
                quantity = quantity,
                price = price
            )
            total = quantity * price

            order.total_bill = total
            order.save()

            product.stock -= quantity
            product.save()

    return order


        
