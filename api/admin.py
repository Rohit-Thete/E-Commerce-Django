from django.contrib import admin
from .models import User, Category, Product, Order, OrderItem


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "role", "email", "phone"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "stock"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "status", "total_bill", "date_created"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price"]
