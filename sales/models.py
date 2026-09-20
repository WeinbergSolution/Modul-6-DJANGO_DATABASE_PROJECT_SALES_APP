from django.db import models

# Customer -> ONE in der One-to-Many Beziehung mit Order
# Ein Customer kann mehrere Orders haben.
# Customer 1 → n Order
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.EmailField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)



# Product -> MANY in der Many-to-Many Beziehung mit Order
# Ein Product kann in mehreren Orders vorkommen.

class Product(models.Model):
#   Macht es sin das Product eine Liste von Order hat = nein
#   Macht es sinn das Orders eine Liste von Product hat = ja
#       daher implementieren wir in Order die liste von Product.

    name = models.CharField(max_length=30)
    price = models.FloatField()



# Bill -> ONE in der One-to-One Beziehung mit Order
# Eine Bill kann genau einer Order zugeordnet sein.

class Bill(models.Model):

    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)




# Order -> MANY in der One-to-Many Beziehung mit Customer
# Order <-> Product = Many-to-Many
# Order <-> Bill = One-to-One

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

#   Hier geben wir der classe Orders eine Liste von Product mit
#   Wichtig: Die class Product muss vor Order definiert sein, wegen der 
#   Beziehung, sont ist der Parameter (Product) undefiniert.   
# 
#   through="Producttype" sagt Django: Für die Many-to-Many-Beziehung soll ein 
#   eigenes Zwischenmodel verwendet werden. Dadurch können wir zusätzliche 
#   Informationen zur Beziehung speichern – hier type_name.
    products = models.ManyToManyField(Product, through="Producttype")

#   Verbindet es über den ForeignKey mit Bill
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)



# Producttype -> Zwischenmodel der Many-to-Many Beziehung
# Verbindet Order und Product miteinander und speichert zusätzliche Daten.

class Producttype(models.Model):
#   Man kann mehrer classen verketten mit (through()), welches in der zwischen
#   classe gesetzt werden muss, in dem fall in Order

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=30) 
    







    