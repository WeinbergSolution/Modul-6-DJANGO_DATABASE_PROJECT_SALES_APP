### -------- BACKEND 6 - Django Datenbank und Adminpane ---------------- ###

## --------------- Sektion 2 Relationships --------------------##

# ------------ 01 - One-to-Many (ForeignKey) -------------- #


# Doku:
# https://docs.djangoproject.com/en/6.1/topics/db/models/
# https://docs.djangoproject.com/en/6.1/topics/db/examples/many_to_one/


# Bei einer One-to-Many Beziehung kann ein Objekt mit mehreren
# Objekten eines anderen Models verbunden sein.

# Beispiel:
# Ein Customer kann mehrere Orders haben.
# Eine Order gehört aber nur zu einem Customer.

# Customer -> ONE
# Order    -> MANY


class Order(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )


# Der ForeignKey wird auf der MANY-Seite angelegt.
# Hier verweist jede Order auf einen Customer.


# Primary Key:
# -> Eindeutige ID eines Datensatzes in seiner eigenen Tabelle.

# Foreign Key:
# -> Verweist auf den Primary Key eines Datensatzes
#    aus einer anderen Tabelle.


# on_delete=models.CASCADE:
# Wird ein Customer gelöscht, werden auch alle Orders gelöscht,
# die mit diesem Customer verbunden sind.


# Das gleiche Prinzip können wir z.B. bei Manufacturer verwenden:

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )


# Kurz zusammengefasst:

# Customer -> kann mehrere Orders haben
# Order    -> gehört zu einem Customer
# ForeignKey -> stellt die Verbindung her
# CASCADE  -> löscht abhängige Einträge mit




# ------------------ 02 - Many-to-Many -------------------- #


# Doku:
# https://docs.djangoproject.com/en/6.1/topics/db/models/


# Bei einer Many-to-Many Beziehung können mehrere Objekte
# mit mehreren anderen Objekten verbunden sein.


class Product(models.Model):

    name = models.CharField(max_length=30)
    price = models.FloatField()


# Eine Order kann mehrere Products enthalten.
# Gleichzeitig kann ein Product in mehreren Orders vorkommen.
# Daher verwenden wir eine Many-to-Many Beziehung.


class Order(models.Model):

    products = models.ManyToManyField(Product)


# ManyToManyField(Product) ermöglicht es einer Order,
# mehrere Products zuzuordnen.


# Wichtig:
# Wenn wir Product direkt verwenden, muss die Klasse Product
# vorher definiert sein.

    products = models.ManyToManyField(Product)


# Alternativ kann der Modelname als String angegeben werden:

    products = models.ManyToManyField("Product")


# Kurz zusammengefasst:

# Order   -> kann mehrere Products haben
# Product -> kann in mehreren Orders vorkommen
# ManyToManyField -> stellt diese Beziehung her





# ------------- 03 - Many-to-Many (through) --------------- #


# Mit through können wir für eine Many-to-Many Beziehung
# ein eigenes Zwischenmodel verwenden.

class Order(models.Model):

    products = models.ManyToManyField(Product, through="Producttype")


# Producttype ist das Zwischenmodel zwischen Order und Product.
# Dadurch können wir der Beziehung zusätzliche Informationen
# wie type_name hinzufügen.

class Producttype(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=30)


# through="Producttype"
# -> verwendet Producttype als eigenes Zwischenmodel

# order und product
# -> verbinden die beiden Models über ForeignKeys

# type_name
# -> zusätzliche Information zur Verbindung

# Ohne through erstellt Django die Zwischentabelle automatisch.
# Mit through können wir diese Verbindung selbst definieren und erweitern.





# ------------------- 04 - One-to-One --------------------- #


# Doku One-to-One Relationships:
# https://docs.djangoproject.com/en/6.1/topics/db/models/


# Bei einer One-to-One Beziehung wird ein Objekt
# genau einem anderen Objekt zugeordnet.


class Bill(models.Model):

    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)


class Order(models.Model):

    bill = models.OneToOneField(
        Bill,
        on_delete=models.CASCADE
    )


# Eine Order besitzt genau eine Bill.
# Eine Bill kann gleichzeitig nur mit einer Order verbunden sein.

# OneToOneField stellt diese eindeutige Verbindung her.

# on_delete=models.CASCADE:
# Wird die verknüpfte Bill gelöscht, wird auch die damit
# verbundene Order gelöscht.


# Kurz zusammengefasst:

# Order -> eine Bill
# Bill  -> eine Order
# OneToOneField -> stellt die 1-zu-1 Beziehung her





# ------------ 05 - Datenbank füllen und prüfen ----------- #


# Zuerst erstellen und übernehmen wir die Migrationen:

    python manage.py makemigrations
    python manage.py migrate


# Anschließend erstellen wir im Projektordner die fill_db.py.
# Der Inhalt befindet sich im Anhang zum Video und in diesem Project

# Die Datei enthält Beispieldaten für:
# Customer, Product, Bill, Order und Producttype.


# Danach starten wir die Django Shell:

    python manage.py shell


# Alle Orders abrufen:

    orders = Order.objects.all()

# Alle Products der ersten Order abrufen:

    orders[0].products.all()


# orders[0].products alleine gibt nur den ManyRelatedManager zurück.
# Mit .all() bekommen wir die tatsächlich verbundenen Products.


# Falls die Testdaten wieder gelöscht werden sollen:

    Producttype.objects.all().delete()
    Order.objects.all().delete()
    Bill.objects.all().delete()
    Customer.objects.all().delete()
    Product.objects.all().delete()






# -------------- 06 - __str__ überschreiben ----------------- #


# Mit __str__ können wir festlegen, wie ein Objekt als String
# bzw. als kurze lesbare Darstellung ausgegeben wird.

class Customer(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.EmailField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Danach starten wir die Django Shell:

    python manage.py shell


# Model importieren:

    from sales.models import Customer


# Alle Customer anzeigen:

    Customer.objects.all()


# Vorher:
# <QuerySet [<Customer: Customer object (1)>, ...]>

# Mit unserer __str__ Methode:
# <QuerySet [<Customer: John Doe>, <Customer: Jane Smith>,
#            <Customer: Alice Johnson>]>


# __str__ macht die Darstellung unserer Model-Objekte
# übersichtlicher und besser lesbar.






# -------------- 07 - _set.all() und CASCADE ---------------- #


# Django Shell öffnen:

    python manage.py shell


# Customer und Orders anzeigen:

    Customer.objects.all()
    Order.objects.all()


# Einen Customer auswählen:

    customer = Customer.objects.all()[0]


# Über order_set können wir von einem Customer auf seine
# zugehörigen Orders zugreifen:

    customer.order_set.all()

# Beispiel:
# <QuerySet [<Order: Order object (1)>]>


# order_set ist die automatisch von Django erzeugte Rückwärtsbeziehung.
# Customer besitzt selbst keinen ForeignKey zu Order,
# aber Order besitzt einen ForeignKey zu Customer.


# Löschen wir den Customer:

    customer.delete()

# werden durch on_delete=models.CASCADE auch seine Order
# und davon abhängige Producttype-Einträge gelöscht.


# Danach können wir das Ergebnis prüfen:

    Customer.objects.all()
    Order.objects.all()


# Kurz:
# customer.order_set.all() -> alle Orders des Customers
# CASCADE                  -> löscht abhängige Objekte mit






#                       Sektion 2 Done
