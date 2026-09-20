from django.contrib import admin
from .models import Customer, Product, Bill, Order, Producttype

# Register your models here.

#   aus classe Customer machen wir eine Admin class die von ModelAdmin erben 
#   wird, das ermöglicht uns filter ein zu bauen im AdminPanel
#   list_filter = baut filter ein im Adminpanel rechts im Filter menü.
#   list_display = Zeigt bezeichnete Spalten in der Tabellenansicht an.
#   fields = ermöglicht es zu definieren, welche inputfelder angezeigt werden.
#   fieldsets = ermöglicht fields mit rein zu nehme auch auch advance Options, 
#   Ausklapbare extra felder im adminpanel die unter einem Hide Butten 
#    versteckt sind 
class CustomerAdmin(admin.ModelAdmin):
    list_filter=['first_name', "last_name"]
    list_display=['last_name', 'account']
#   fields=['first_name', "last_name", 'account']
    fieldsets = [
        (
            None,
            {
                "fields": ['first_name', "last_name", 'account'],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ['collapse'],
                'fields': ['newsletter_abo'],
            },
        ),
    ]






#   Hiermit regestrieren wir alle Nutzer aus der Tabelle Customer im Admin 
#   pannel 
admin.site.register(Customer,CustomerAdmin )
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Producttype)
