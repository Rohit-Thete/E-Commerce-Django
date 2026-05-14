from django.contrib.auth.base_user import BaseUserManager

from django.db import models



class CustomUserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class CustomOrderManager(models.Manager):
    def get_queryset(self):
        from .models import OrderStatus
        return super().get_queryset().filter(status=OrderStatus.DELIVERED)
