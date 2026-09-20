from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer

# Create your views here.


class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"