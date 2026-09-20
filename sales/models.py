from django.db import models

# Customer -> ONE in der One-to-Many Beziehung mit Order
# Ein Customer kann mehrere Orders haben.
# Customer 1 → n Order

#   help_text wird unter dem eingabefeld im Adminpanel ein Hinweistext 
#   eingebelndet.
#   error_messages zeigt fehler an z.b bei validation
class Customer(models.Model):
    first_name = models.CharField(max_length=30,error_messages="hoppla",help_text='max 30 letters, dummy')
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.EmailField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)
    slug = models.SlugField(blank=True, default="")



# In der models.py können wir über die Meta-Klasse
# zusätzliche Einstellungen für unser Model festlegen.

#   verbose_name_plural = ermöglicht 
# ordering bestimmt die Standardsortierung.
# Das "-" vor first_name bedeutet absteigend.

# verbose_name bestimmt den Namen eines einzelnen Objekts.
# verbose_name_plural bestimmt den Namen in der Mehrzahl.


    class Meta:
        verbose_name= 'Customer'
        verbose_name_plural= 'Customers'
        ordering=['-first_name']





#   Hiermit können wir die ausgabe der shell besser machen, schöner
#   Zeitgleich hat es ein einfluss auf die visualisierung im AdminPanel
#   In dem fall das first und lastname angezeigt werden bei jedem einzelnen 
#   Eintrag
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




#   damit lässt sich die save Funtion überschreiben wenn ich im AdminPanel das 
#   Account feld ausfülle und auf save klicke. 
#   Background color für user Profile z.b. random generiern z.b.

#   Wichtig ist nur: Wenn save() überschrieben wird, sollte man *args, **kwargs 
#   mitnehmen und an super().save() weitergeben.
def save(self):
    self.account = 651681
    return super().save()




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

    def __str__(self):
        return f"{self.name} ({self.price})"


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
    
    def __str__(self):
        return f"{self.type_name}"






    