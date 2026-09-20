from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer

# Create your views here.


class CustomerListView(ListView):
    model = Customer
    # queryset = Customer.objects.all() = das gleiche wie darüber
    template_name = "sales/list.html"

    #   gibt nur 2 einträge zurück aus der Liste, super praktiisch um das  
    #   ganze einzugränzen 
    paginate_by = 2


class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get("name")
        return Customer.objects.filter(first_name__icontains=name)