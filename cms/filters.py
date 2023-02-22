# products/filters.py
from decimal import Decimal
from django.db.models import Q
import django_filters
from .models import Customer

class CustomerFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Customer
        fields = ['query']

    def universal_search(self, queryset, name, value):
        return Customer.objects.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value)
        )
