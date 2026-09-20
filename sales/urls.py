from django.urls import path
from .views import CustomerListView, CustomerListSearchView




urlpatterns = [
    path('', CustomerListView.as_view()),
    path('<str:name>', CustomerListSearchView.as_view())
]
