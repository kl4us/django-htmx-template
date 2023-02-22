from django.shortcuts import render

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import Customer
from .tables import CustomerHTMxTable
from .filters import CustomerFilter

class CustomerHTMxTableView(SingleTableMixin, FilterView):
    table_class = CustomerHTMxTable
    queryset = Customer.objects.all()
    filterset_class = CustomerFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "cms/customer_table_partial.html"
        else:
            template_name = "cms/customer_table_htmx.html"

        return template_name
