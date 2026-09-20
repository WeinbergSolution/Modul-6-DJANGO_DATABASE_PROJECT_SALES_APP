from django.urls import path
from .views import CustomerListView, CustomerListSearchView, CustomerDetailView




urlpatterns = [
    path('', CustomerListView.as_view()),
    path('<str:name>', CustomerListSearchView.as_view()),
    # wichtig ist das der int:pk = der primary key ist 
    path('customer/<int:pk>/', CustomerDetailView.as_view()),
]
