import django_filters
from .models import Order, Product


class OrderFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name="status")

    class Meta:
        model = Order
        fields = ["status", "date_created", "total_bill"]


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name")
    price = django_filters.NumberFilter(field_name="price")
    stock = django_filters.NumberFilter(field_name="stock")
    category = django_filters.CharFilter(field_name="category__name")
    available=django_filters.BooleanFilter(method="filter_available")

    class Meta:
        model = Product
        fields = ["name", "price", "stock","category__name","available"]


    def filter_available(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset.filter(stock=0)
