# products/tables.py
import django_tables2 as tables
from .models import Customer

class CustomerHTMxTable(tables.Table):
    class Meta:
        model = Customer
        template_name = "tables/bootstrap_htmx.html"
