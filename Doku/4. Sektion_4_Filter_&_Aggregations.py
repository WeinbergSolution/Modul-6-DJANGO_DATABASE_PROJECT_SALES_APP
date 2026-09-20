### -------- BACKEND 6 - Django Datenbank und Adminpane ---------------- ###

# --------------- Sektion 4: Filter & Aggregations -------------------- #


# ------------------- 01 - Einführung ------------------------- #


# In dieser Sektion beschäftigen wir uns intensiver mit Queries
# und QuerySets in Django.

# Queries ermöglichen die Kommunikation mit unserer Datenbank.
# Über QuerySets können wir Daten abrufen, filtern, sortieren
# und später auch aggregieren.

# Ein gutes Verständnis davon ist für die Arbeit mit
# Django und Datenbanken essenziell.


# Django QuerySet Doku:
# https://docs.djangoproject.com/en/6.1/ref/models/querysets/






# -------------- 02 - Datenbank vorbereiten ------------------- #


# Für die nächsten Übungen bereiten wir unsere Datenbank vor
# und entfernen vorerst einige Funktionen aus den vorherigen Sektionen.


# models.py

# Folgende Sachen auskommentieren bzw. entfernen:

# class Meta

# def save(self, *args, **kwargs)

# slug-Feld:
# slug = models.SlugField(blank=True, default="")


# admin.py

# prepopulated_fields entfernen:
# prepopulated_fields = {'slug': ['first_name', 'last_name']}

# Zusätzlich 'slug' aus den fieldsets entfernen.


# Danach erstellen und übernehmen wir die Änderungen:

    python manage.py makemigrations
    python manage.py migrate


# Django Shell starten:

    python manage.py shell


# Models importieren:

    from sales.models import Product, Producttype, Bill, Order, Customer


# Zuerst löschen wir die vorhandenen Testdaten.

# Anschließend befüllen wir die Datenbank wieder mit den
# aktuellen Beispieldaten aus unserer fill_db.py.


# Damit haben wir eine saubere Ausgangsbasis für die
# kommenden Query-, Filter- und Aggregation-Übungen.
    





# ------------ 03 - Wiederholung von get() und all() ----------------- #


# Django Shell starten:

    python manage.py shell


# Models importieren:

    from sales.models import Product, Producttype, Bill, Order, Customer


# Mit all() bekommen wir alle Einträge eines Models:

    Customer.objects.all()

# Ergebnis:
# <QuerySet [<Customer: John Doe>, <Customer: Jane Smith>,
#            <Customer: Alice Johnson>]>


# Mit get() können wir einen bestimmten Eintrag abrufen:

    Customer.objects.get(first_name="John")

# Ergebnis:
# <Customer: John Doe>


# Bei der Schreibweise müssen wir auf Groß- und Kleinschreibung achten.

    Customer.objects.get(first_name="john")

# Findet in unserem Beispiel keinen passenden Customer:

# Customer.DoesNotExist:
# Customer matching query does not exist.


# Kurz:
# all() -> gibt alle passenden Datensätze als QuerySet zurück
# get() -> erwartet genau einen passenden Datensatz






# -------------- 04 - Filter (kleiner, größer usw.) ------------------- #


# Mit filter() können wir QuerySets nach bestimmten Bedingungen filtern.

# Beispiel: Alle bezahlten Rechnungen:

    Bill.objects.filter(is_paid=True)


# Vergleichsoperatoren wie < oder > können nicht direkt
# innerhalb von filter() verwendet werden:

    Bill.objects.filter(total_amount < 105)

# Das funktioniert nicht.


# Dafür verwendet Django sogenannte Field Lookups mit __

# Kleiner als:
    Bill.objects.filter(total_amount__lt=105)

# Kleiner oder gleich:
    Bill.objects.filter(total_amount__lte=100)

# Größer als:
    Bill.objects.filter(total_amount__gt=100)

# Größer oder gleich:
    Bill.objects.filter(total_amount__gte=100)


# Kurz:
# __lt  -> less than            <
# __lte -> less than or equal   <=
# __gt  -> greater than         >
# __gte -> greater than or equal >=


# Wichtig:
# "__" wird von Django für Lookups und Beziehungen verwendet.
# Deshalb sollten Feldnamen selbst keine doppelten Unterstriche enthalten.




# ---------------- 05 - SQL anzeigen lassen (.query) ------------------ #


# Mit .query können wir uns anschauen, welches SQL Django
# aus unserem QuerySet erzeugt.


# Normale Abfrage:

    Customer.objects.filter(first_name="John")


# Die gleiche Abfrage mit dem Lookup __exact:

    Customer.objects.filter(first_name__exact="John")


# __exact bedeutet, dass der Wert exakt übereinstimmen soll.
# Wenn wir keinen Lookup angeben, verwendet Django standardmäßig exact.

# Deshalb sind diese beiden Abfragen gleich:

    Customer.objects.filter(first_name="John")
    Customer.objects.filter(first_name__exact="John")


# Mit .query bekommen wir das erzeugte SQL:

    Customer.objects.filter(first_name="John").query


# Mit str() können wir es als String ausgeben:

    str(Customer.objects.filter(first_name="John").query)


# Beide Varianten erzeugen entsprechend die gleiche SQL-Abfrage:

    str(Customer.objects.filter(first_name__exact="John").query)
    str(Customer.objects.filter(first_name="John").query)


# Kurz:
# __exact -> exakte Übereinstimmung
# ohne Lookup wird standardmäßig exact verwendet
# .query   -> zeigt das von Django erzeugte SQL
# str()    -> gibt dieses SQL als String aus




# ------------------- 06 - limit und offset ---------------------- #


# Bei QuerySets können wir einen Start- und Endpunkt festlegen.

    Bill.objects.all()


# Einen einzelnen Eintrag über den Index abrufen:

    Bill.objects.all()[2]

# Gibt direkt ein einzelnes Bill-Objekt zurück.


# Die ersten zwei Einträge:

    Bill.objects.all()[:2]


# Ab Index 2 bis vor Index 3:

    Bill.objects.all()[2:3]

# Gibt ein QuerySet mit einem Eintrag zurück.


# Mehrere Einträge:

    Bill.objects.all()[2:5]


# Wichtig:
# [2]   -> gibt direkt ein einzelnes Objekt zurück
# [2:3] -> gibt ein QuerySet mit einem Objekt zurück


# Wenn das QuerySet genau einen Eintrag enthält,
# können wir diesen mit get() abrufen:

    Bill.objects.all()[2:3].get()

# Ergebnis entspricht in unserem Beispiel:

    Bill.objects.all()[2]


# Django übersetzt das Slicing im Hintergrund in SQL
# mit LIMIT und OFFSET.

# [:2]  -> LIMIT
# [2:5] -> OFFSET + LIMIT



# --------------- 07 - Q function (OR, AND, NOT) ------------------- #


# Mit Q können wir komplexere Bedingungen in Queries erstellen.

from django.db.models import Q


# Mehrere Bedingungen in filter() entsprechen standardmäßig AND:

    Bill.objects.filter(is_paid=True, total_amount__gt=100)


# Das Gleiche können wir mit Q und & schreiben:

    Bill.objects.filter(
        Q(is_paid=True) & Q(total_amount__gt=100)
    )


# Mit | können wir ein OR erzeugen:

    Bill.objects.filter(
        Q(is_paid=True) | Q(total_amount__gt=100)
    )


# Mit ~ können wir eine Q-Bedingung negieren (NOT):

    Bill.objects.filter(~Q(is_paid=True))


# exclude() schließt passende Datensätze aus:

    Bill.objects.exclude(
        Q(is_paid=True) | Q(total_amount__gt=100)
    )


# Kurz:
# &       -> AND
# |       -> OR
# ~Q(...) -> NOT
# exclude -> schließt passende Datensätze aus 





# ----- 08 - Filter bei Verschachtelungen (Many-to-Many, One-to-One) ----- #


# Auch über Beziehungen zwischen Models können wir filtern.


# Über order_set bekommen wir die Orders eines Customers:

    Customer.objects.all()[0].order_set.all()


# Beispiel: Orders des dritten Customers:

    Customer.objects.all()[2].order_set.all()


# Über __ können wir auf Felder eines verbundenen Models zugreifen.

# Nur Orders mit bezahlter Bill:

    Customer.objects.all()[2].order_set.filter(
        bill__is_paid=True
    )


# Nur Orders mit unbezahlter Bill:

    Customer.objects.all()[2].order_set.filter(
        bill__is_paid=False
    )


# Wir können dabei auch weitere Lookups verwenden:

    Customer.objects.all()[2].order_set.filter(
        bill__total_amount__lt=150
    )

    Customer.objects.all()[2].order_set.filter(
        bill__total_amount__gte=150
    )


# Dabei bedeutet:

# bill__is_paid
# -> gehe zur verbundenen Bill
# -> prüfe das Feld is_paid

# bill__total_amount__gte
# -> gehe zur verbundenen Bill
# -> nehme das Feld total_amount
# -> prüfe mit gte (größer oder gleich)


# Beziehungen und Lookups können also mit __ kombiniert werden.




# ------------------- 09 - order_by() ------------------------- #


# Mit order_by() können wir unsere QuerySets sortieren.


# Aufsteigend nach first_name:

    Customer.objects.order_by("first_name")


# Absteigend nach first_name:

    Customer.objects.order_by("-first_name")


# Auch nach anderen Feldern können wir sortieren:

    Customer.objects.order_by("last_name")


# Das "-" vor dem Feldnamen dreht die Sortierreihenfolge um.

# "first_name"  -> aufsteigend
# "-first_name" -> absteigend


# Auch über Beziehungen hinweg können wir sortieren.

# Orders nach dem total_amount ihrer Bill:

    Order.objects.order_by("bill__total_amount")

# Absteigend:

    Order.objects.order_by("-bill__total_amount")


# Ebenso können wir nach der ID der verbundenen Bill sortieren:

    Order.objects.order_by("bill__id")

    Order.objects.order_by("-bill__id")


# Kurz:
# order_by("feld")  -> aufsteigend
# order_by("-feld") -> absteigend
# __                 -> Sortierung über verbundene Models




# ------------ 10 - Aggregations (Avg, Count usw.) ------------------- #


# Aggregations ermöglichen Berechnungen über unsere Datenbank.

# Doku:
# https://docs.djangoproject.com/en/6.1/topics/db/aggregation/


# Dafür importieren wir z.B. Avg oder Count:

from django.db.models import Avg, Count


# Mit aggregate() können wir z.B. den Durchschnitt berechnen:

    Bill.objects.aggregate(Avg("total_amount", default=0))

# Ergebnis:
# {'total_amount__avg': 120.0}

# aggregate() gibt uns hier ein Dictionary mit dem Ergebnis zurück.


# Mit annotate() können wir jedem Objekt einen zusätzlich
# berechneten Wert hinzufügen.

    orders = Customer.objects.annotate(
        num_orders=Count("order")
    )


# Danach können wir die Anzahl der Orders eines Customers abrufen:

    orders[0].num_orders
    # 1

    orders[1].num_orders
    # 1

    orders[2].num_orders
    # 3


# Kurz:
# aggregate() -> berechnet einen Gesamtwert über ein QuerySet
# annotate()  -> fügt jedem Objekt einen berechneten Wert hinzu
# Avg()       -> Durchschnitt
# Count()     -> Anzahl



# ------------------- 11 - Datenbank optimal nutzen --------------------- #


# Bei Datenbankabfragen sollten wir darauf achten,
# unnötige Zugriffe auf die Datenbank zu vermeiden.

# Doku:
# https://docs.djangoproject.com/en/6.1/topics/db/optimization/


# Bereits geladene Daten können von Django teilweise gecacht werden.

    entry = Entry.objects.get(id=1)

    entry.blog
    entry.blog

# Beim ersten Zugriff wird blog geladen.
# Weitere Zugriffe können den bereits geladenen Wert verwenden.


# Bei QuerySets bzw. Beziehungen sollte man Ergebnisse,
# die mehrfach benötigt werden, zwischenspeichern.

    members = group.members.all()

# Danach verwenden wir immer wieder members,
# statt die Abfrage unnötig neu aufzubauen.

    if members:
        for member in members:
            print(member.username)


# Generell:
# Wenn möglich, mehrere Datenbankoperationen zusammenfassen
# und unnötige Queries vermeiden.


# Auch beim Erstellen vieler Datensätze können wir
# Datenbankzugriffe reduzieren.

# Viele einzelne Inserts:

    Product.objects.create(...)
    Product.objects.create(...)
    Product.objects.create(...)

# Bei vielen Objekten ist bulk_create() effizienter:

    Product.objects.bulk_create([
        Product(...),
        Product(...),
        Product(...),
    ])


# Kurz:
# -> unnötige Datenbankzugriffe vermeiden
# -> QuerySets sinnvoll wiederverwenden
# -> Abfragen möglichst effizient gestalten
# -> bei vielen Objekten Bulk-Methoden verwenden


# ------------------- Sektion 4 abgeschlossen ------------------- #


