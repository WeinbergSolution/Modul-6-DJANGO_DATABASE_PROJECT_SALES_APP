from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.EmailField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)

class Order(models.Model):
#   Ein Customer kann mehrer Orders haben, ein Order aber nur einen Customer

#   Customer = one
#   Order = Many

#   ForeingKey = Fremder Schlüssel aus der Liste Customer, er kann gleich 
#   aussehn wie der Primarykey in Order, ist aber aus Customer


#   PrimaryKey = ist wiederum die ID, die ein einzelnes Element aus Order
#   oder Customer definiert. Ist der Schlüssel zu dem Object

#   on_delete=models.CASCADE = 
#   wenn der Customer gelöscht wird, wird auch die Order gelöscht
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    