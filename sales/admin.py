from django.contrib import admin
from .models import Customer, Product, Bill, Order, Producttype

# Register your models here.

#   Hiermit regestrieren wir alle Nutzer aus der Tabelle Customer im Admin 
#   pannel 
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Producttype)
