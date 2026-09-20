from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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


from django.utils import timezone

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "sales/detail.html"

    def get_object(self):
        obj = super().get_object()

        # hier bekommen wir die komplete time raus, wird in der detail.html ausgegeben, wichtig wird nur angezeigt aber nicht in der db 
        # gesichert 
        obj.last_accessed = timezone.now()
        return obj



    
