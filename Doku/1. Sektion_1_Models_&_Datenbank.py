### -------- BACKEND 6 - Django Datenbank und Adminpane ---------------- ###

## --------------- Sektion 1: Models & Datenbank --------------------##

# ------------   01 - Django Dokumentation -------------- #

#   Django Dokumentation
#   https://docs.djangoproject.com/en/6.1/
#
#   W 3 Scools
#   https://www.w3schools.com/django/django_models.php

#   In den nächsten Sektion von Modul 6, arbeiten wir hauptsächlich mit der Sekt
#   "The model layer"
#   https://docs.djangoproject.com/en/6.1/topics/db/models/





# ------------ 02 - Django Models --------------------- #

# Was sind Models?
#
#   Mit Models definieren wir, was unsere Datenbank beinhaltet
#   und wie die Daten darin aufgebaut sind.
#
#   Unsere Datenbank besteht größtenteils aus Tabellen.
#
#   Zum Test bauen wir eine Sales-App mit einer Datenbank.


# Schritt 1: Projekt anlegen
#
#   Projektordner erstellen und in den Pfad wechseln.
#
#   Virtuelle Umgebung erstellen:
#       python -m venv env
#
#   Virtuelle Umgebung aktivieren:
#       env\Scripts\activate
#
#   Prüfen, ob die virtuelle Umgebung läuft:
#       pip freeze
#
#   Django installieren:
#       pip install django
#
#   Django-Version prüfen:
#       django-admin --version
#
#   Django-Projekt erstellen:
#       django-admin startproject database_project .
#
#   Sales-App erstellen:
#       python manage.py startapp sales
#
#   Sales-App Regestrieren in settings.py unter INSTALLED_APPS
#        'sales'   
#
#   Installierte Pakete in requirements.txt speichern:
#       pip freeze > requirements.txt
#
#   .gitignore anlegen.
#
#   Git-Repository anlegen und Projekt pushen.


# Schritt 2: Models anlegen = Tabellen in der Datenbank
#
#   Models werden in der models.py unserer App angelegt.
#
#   Beispiel:
#
#       class Customer(models.Model):
#           first_name = models.CharField(max_length=30)
#           last_name = models.CharField(max_length=30)
#
#
#   Customer erbt von models.Model.
#
#   Die Klasse Customer beschreibt damit den Aufbau unserer Tabelle.
#
#   first_name und last_name sind Spalten der Tabelle.
#
#       CharField       = Text / String
#       max_length=30   = maximal 30 Zeichen
#
#   Wir haben also eine Klasse, die klar definiert, wie ein Objekt
#   bzw. ein Datensatz in unserer Customer-Tabelle aussehen soll.
#
#   Vereinfacht:
#
#       Customer
#       -------------------------
#       first_name | last_name
#       -------------------------
#       Pascal     | Weinberg
#       Max        | Mustermann
#
#
#   Model-Klasse   -> Tabelle
#   Attribut       -> Spalte
#   Objekt         -> Datensatz / Zeile




# --------- 03 - makemigrations und migrate ----------- #

#   Nachdem wir unser Model erstellt haben, müssen die Änderungen
#   für die Datenbank vorbereitet und anschließend ausgeführt werden.


#   Migration erstellen:
#
#       python manage.py makemigrations
#
#   Sollte die Meldung "No changes detected" kommen, kann es daran liegen,
#   dass die App noch nicht in der settings.py unter INSTALLED_APPS
#   registriert wurde.


#   0001_initial.py
#
#       Django erstellt unter sales/migrations/ die Datei 0001_initial.py.
#
#       Die Migration enthält unser Customer-Model mit den Fields,
#       die wir in models.py definiert haben:
#
#           first_name
#           last_name
#
#       Zusätzlich generiert Django automatisch ein ID-Field.
#       Diese ID dient als Primary Key und identifiziert jeden Datensatz
#       eindeutig.


#   Migration auf die Datenbank anwenden:
#
#       python manage.py migrate
#
#   Dadurch werden die Migrationen ausgeführt und unsere SQLite-Datenbank
#   db.sqlite3 erstellt bzw. aktualisiert.
#
#   Um die Datenbank direkt in VS Code anzusehen, verwenden wir:
#
#       SQLite Viewer – Florian Klampfer
#
#   In der db.sqlite3 finden wir jetzt unter anderem unsere Tabelle:
#
#       sales_customer
#
#   Sie enthält aktuell die Spalten:
#
#       id
#       first_name
#       last_name
#
#   Datensätze sind natürlich noch keine vorhanden.


#   Merke:
#
#       makemigrations = Änderungen an Models erkennen und
#                        Migrationsdateien erstellen
#
#       migrate        = Migrationen auf die Datenbank anwenden
#
#       models.py      -> definiert den Aufbau
#       Migration      -> beschreibt die Änderung
#       db.sqlite3     -> enthält die tatsächlichen Daten




# ----------------- 04 - Field Types ------------------- #

#   Django stellt verschiedene Field Types zur Verfügung.
#   Mit ihnen definieren wir, welche Art von Daten eine Spalte
#   in unserer Datenbank enthalten soll.
#
#   Doku:
#   https://docs.djangoproject.com/en/6.1/ref/models/fields/#model-field-types


#   Einige wichtige Field Types:
#
#   BigAutoField
#       Automatisch hochzählende Ganzzahl, wird häufig für die ID
#       bzw. den Primary Key verwendet.
#
#   BigIntegerField
#       Ganzzahl für besonders große positive oder negative Zahlen.
#
#   BinaryField
#       Speichert Binärdaten, also Daten in Form von Bytes.
#
#   BooleanField
#       Speichert True oder False.
#
#   CharField
#       Speichert Text / Strings mit einer festgelegten maximalen Länge.
#
#   DateField
#       Speichert ein Datum.
#
#   DateTimeField
#       Speichert Datum und Uhrzeit.
#
#   DecimalField
#       Speichert Dezimalzahlen mit festgelegter Genauigkeit,
#       z.B. gut für Geldbeträge.
#
#   DurationField
#       Speichert eine Zeitdauer.
#
#   EmailField
#       Speichert eine E-Mail-Adresse und prüft deren Format.
#
#   FileField
#       Speichert bzw. verwaltet hochgeladene Dateien.
#
#   FieldFile
#       Repräsentiert eine Datei, die über ein FileField gespeichert wurde.
#
#   FilePathField
#       Speichert bzw. wählt einen Dateipfad aus einem bestimmten Verzeichnis.
#
#   FloatField
#       Speichert Fließkommazahlen.
#
#   GeneratedField
#       Wert wird von der Datenbank aus anderen Feldern berechnet.
#
#   GenericIPAddressField
#       Speichert IPv4- oder IPv6-Adressen.
#
#   ImageField
#       Wie FileField, speziell für Bilder.
#
#   IntegerField
#       Speichert Ganzzahlen.
#
#   JSONField
#       Speichert Daten im JSON-Format.
#
#   TimeField
#       Speichert eine Uhrzeit.
#
#   ... und viele weitere.
#   https://docs.djangoproject.com/en/6.1/ref/models/fields/#model-field-types


#   Unser Customer-Model erweitern wir jetzt um weitere Field Types:
#
#       class Customer(models.Model):
#           first_name = models.CharField(max_length=30)
#           last_name = models.CharField(max_length=30)
#           newsletter_abo = models.BooleanField()
#           email_address = models.EmailField()
#           account = models.FloatField()
#
#
#   Damit enthält Customer jetzt:
#
#       first_name       -> Text
#       last_name        -> Text
#       newsletter_abo   -> True / False
#       email_address    -> E-Mail-Adresse
#       account          -> Fließkommazahl
#
#
#   Wichtig:
#       Der Field Type bestimmt, welche Art von Daten in einer
#       Spalte gespeichert werden kann.





# ------------ 05 - CREATE (save(), objects.create()) -------------- #


# Wir kommentieren die eben hinzugefügten Felder erst einmal aus,
# da wir diese noch nicht migriert haben.

# newsletter_abo = models.BooleanField()
# email_address = models.EmailField()
# account = models.FloatField()


# Nun geben wir in der Konsole folgenden Befehl ein:

    python manage.py shell

# Die Django Shell dient dazu, direkt mit unserem Django-Projekt zu arbeiten.
# Dadurch können wir unter anderem unsere Models verwenden und über das
# Django ORM Einträge in der Datenbank erstellen, auslesen, verändern oder löschen.


# Nachdem die Shell gestartet wurde, geben wir Folgendes ein:

    from sales.models import Customer

# Damit importieren wir unser Customer Model und können nun direkt über
# die Shell darauf zugreifen.


# Als Nächstes erstellen wir ein Customer-Objekt:

    first_customer = Customer(first_name="Mandy", last_name="Musterfrau")

# Dadurch wurde noch nichts in der Datenbank gespeichert.
# Wir haben zunächst nur ein Objekt erstellt, welches auf unserem
# Customer Model basiert.

# Damit der Customer tatsächlich in der db.sqlite3 gespeichert wird,
# müssen wir das Objekt noch speichern:

    first_customer.save()


# Eine weitere Möglichkeit bietet der Object Manager von Django.
# Mit objects.create() können wir einen Customer direkt erstellen und speichern:

    Customer.objects.create(first_name="Rudolf", last_name="Mustermann")

# Das ist der Shortcut für:

    customer = Customer(first_name="Rudolf", last_name="Mustermann")
    customer.save()


# Sollte etwas schiefgehen oder beispielsweise ein Eintrag doppelt
# vorhanden sein, können wir einen bestimmten Customer über seine ID löschen:

    Customer.objects.get(id=2).delete()

# get(id=2) sucht den Customer mit der ID 2.
# delete() löscht diesen anschließend aus der Datenbank.


# Mit objects.all() können wir uns alle vorhandenen Customer-Objekte anzeigen lassen:

    Customer.objects.all()

# Beispielausgabe:

    <QuerySet [<Customer: Customer object (1)>]>


# Wenn wir die genauen Werte der Einträge sehen möchten:

    Customer.objects.values()

# Beispielausgabe:

    <QuerySet [
        {'id': 1, 'first_name': 'Mandy', 'last_name': 'Musterfrau'}
    ]>


# Kurz zusammengefasst:

# Customer(...)                   -> Objekt erstellen, noch nicht gespeichert
# .save()                         -> Objekt in der Datenbank speichern
# Customer.objects.create(...)    -> Objekt erstellen und direkt speichern
# Customer.objects.get(id=2)      -> Bestimmtes Objekt abrufen
# .delete()                       -> Objekt löschen
# Customer.objects.all()          -> Alle Customer-Objekte abrufen
# Customer.objects.values()       -> Die genauen Werte anzeigen






# ------- 06 - clean_fields() (save() und create() validieren) --------- #

# Doku validation
# https://docs.djangoproject.com/en/5.0/ref/models/instances/#validating-objects

# Ein kleines Problem existiert bei unseren Feldern noch.
# Was passiert beispielsweise, wenn wir bei first_name einen Text mit
# mehr als 30 Zeichen speichern, obwohl wir im Model max_length=30 angegeben haben?

    first_name = models.CharField(max_length=30)


# Erstellen wir beispielsweise einen Customer mit einem zu langen Namen:

    second_customer = Customer(
        first_name="DasIstEinVielZuLangerVornameMitMehrAls30Zeichen",
        last_name="Mustermann"
    )


# Django verhindert beim normalen save() nicht automatisch, dass dieser
# zu lange Wert gespeichert wird.

    second_customer.save()


# Obwohl max_length=30 im Model angegeben wurde, führt save() nicht automatisch
# die Model-Validierung aus.


# Wir können die Felder aber vor dem Speichern mit clean_fields() validieren:

    second_customer.clean_fields()


# clean_fields() überprüft die Werte anhand der Regeln, die wir in unserem
# Model festgelegt haben.

# In unserem Fall wird geprüft, ob first_name die maximale Länge von
# 30 Zeichen überschreitet.

# Ist der Wert ungültig, erzeugt Django einen ValidationError.


# Wichtig:
# clean_fields() validiert das Objekt, speichert es aber nicht.

# Wenn clean_fields() einen ValidationError erzeugt, sollten wir das Objekt
# anschließend natürlich nicht speichern.


# Technisch könnten wir danach trotzdem wieder folgendes ausführen:

    second_customer.save()

# Das würde den ungültigen Wert trotzdem speichern, weil save()
# die Model-Validierung nicht automatisch ausführt.


# Deshalb ist die gedachte Reihenfolge:

    second_customer = Customer(
        first_name="Mandy",
        last_name="Musterfrau"
    )

    second_customer.clean_fields()
    second_customer.save()


# Ist alles gültig:
# clean_fields() läuft ohne Fehler durch und danach können wir speichern.

# Ist etwas ungültig:
# clean_fields() erzeugt einen ValidationError und wir können diesen Fehler
# später abfangen und entsprechend behandeln.


# Kurz zusammengefasst:

# clean_fields()  -> Validiert die einzelnen Felder des Models
# ValidationError -> Wird ausgelöst, wenn ein Feld ungültig ist
# save()           -> Speichert das Objekt, validiert aber nicht automatisch
# create()         -> Erstellt und speichert direkt, validiert ebenfalls nicht automatisch




# ----------------- 07 - READ (get() und all()) ------------------- #


# Wie bekommen wir die bereits gespeicherten Daten aus unserer Datenbank?

# Dafür können wir über unser Customer Model und den Object Manager
# auf die gespeicherten Customer zugreifen.


# Mit objects.all() bekommen wir alle vorhandenen Customer aus der Datenbank:

    Customer.objects.all()

# Django gibt uns dabei ein QuerySet mit allen gefundenen Customer-Objekten zurück.

# Beispiel:

    <QuerySet [
        <Customer: Customer object (1)>,
        <Customer: Customer object (2)>
    ]>


# Jeder Customer besitzt eine eindeutige ID.
# Diese ID ist der Primary Key unseres Models und wird von Django
# automatisch angelegt.


# Mit objects.get() können wir einen bestimmten Customer suchen:

    Customer.objects.get(first_name="Mandy")

# Existiert genau ein Customer mit dem Vornamen Mandy, bekommen wir
# dieses Customer-Objekt zurück.

# Beispiel:

    <Customer: Customer object (1)>

# Die (1) zeigt uns dabei die ID des Customer-Objekts.


# Wir können einen Customer auch direkt über seine eindeutige ID abrufen:

    Customer.objects.get(id=1)

# Da die ID der Primary Key ist, kann sie nur einmal vorkommen.
# Dadurch bekommen wir eindeutig genau einen Customer zurück.


# Problem bei get():

# Wenn wir beispielsweise mehrere Customer mit dem gleichen Vornamen haben:

    Customer.objects.get(first_name="Mandy")

# und "Mandy" mehrfach in der Datenbank vorkommt, kann get() nicht
# entscheiden, welchen Customer wir haben möchten.

# Django erzeugt dann einen MultipleObjectsReturned Fehler.


# In diesem Fall können wir entweder über die eindeutige ID gehen:

    Customer.objects.get(id=1)

# oder filter() verwenden, wenn wir mehrere passende Einträge abrufen möchten:

    Customer.objects.filter(first_name="Mandy")


# Kurz zusammengefasst:

# Customer.objects.all()                  -> Alle Customer abrufen
# Customer.objects.get(id=1)              -> Genau einen Customer über die ID abrufen
# Customer.objects.get(first_name="Mandy")-> Genau einen Customer über den Namen suchen
# Customer.objects.filter(first_name="Mandy") -> Alle passenden Customer abrufen

# get()    -> Erwartet genau EIN passendes Objekt
# all()    -> Gibt alle Objekte zurück
# filter() -> Kann mehrere passende Objekte zurückgeben




# ------------- 08 - UPDATE und DELETE ---------------- #


# DELETE - Einträge löschen


# Zuerst können wir uns alle Customer aus der Datenbank holen:

    all_customers = Customer.objects.all()


# Über den Index können wir auf einen bestimmten Customer aus dem
# QuerySet zugreifen und diesen löschen:

    all_customers[1].delete()


# Django gibt uns nach dem Löschen beispielsweise Folgendes zurück:

    (1, {'sales.Customer': 1})

# Die erste 1 bedeutet, dass insgesamt ein Objekt gelöscht wurde.
# {'sales.Customer': 1} zeigt uns, dass ein Customer aus der
# sales App gelöscht wurde.


# Wichtig:
# Der Index [1] ist NICHT die ID des Customer.

# [0] -> erstes Objekt im QuerySet
# [1] -> zweites Objekt im QuerySet
# [2] -> drittes Objekt im QuerySet

# Wenn wir gezielt über die ID löschen möchten, können wir beispielsweise:

    Customer.objects.get(id=2).delete()


# UPDATE - Einträge verändern


# Um einen vorhandenen Customer zu verändern, holen wir uns zunächst
# das gewünschte Objekt aus der Datenbank.

    all_customers = Customer.objects.all()

    single_customer = all_customers[1]


# Nun können wir die einzelnen Werte des Customer verändern:

    single_customer.first_name = "Bifur"
    single_customer.last_name = "Zwergerich"


# Die Änderungen befinden sich zunächst nur in unserem Objekt.
# Damit sie auch in der Datenbank gespeichert werden, verwenden wir:

    single_customer.save()


# save() kann somit sowohl zum Erstellen als auch zum Aktualisieren
# eines Eintrags verwendet werden.


# Beispiel beim Erstellen:

    new_customer = Customer(
        first_name="Mandy",
        last_name="Musterfrau"
    )

    new_customer.save()


# Beispiel beim Aktualisieren:

    single_customer = Customer.objects.get(id=1)

    single_customer.first_name = "Bifur"
    single_customer.last_name = "Zwergerich"

    single_customer.save()


# Kurz zusammengefasst:

# .delete()        -> Löscht ein Objekt aus der Datenbank
# .save()          -> Speichert ein neues Objekt oder Änderungen an einem Objekt
# all_customers[1] -> Zweites Objekt aus dem QuerySet
# get(id=2)        -> Customer mit der eindeutigen ID 2




# ------------ 09 - Defaults setzen / weiteres Field hinzufügen ------------ #

# Wir kommentieren das Field newsletter_abo wieder ein:

    newsletter_abo = models.BooleanField()


# Anschließend versuchen wir eine neue Migration zu erstellen:

    python manage.py makemigrations


# Dies führt allerdings zu einer Meldung wie:

    It is impossible to add a non-nullable field 'newsletter_abo'
    to customer without specifying a default.


# Der Grund dafür ist, dass bereits Customer in unserer Datenbank vorhanden sind.

# Wir fügen mit newsletter_abo eine neue Spalte hinzu.
# Django weiß aber nicht, welchen Wert die bereits vorhandenen Customer
# in dieser neuen Spalte bekommen sollen.

# Ein BooleanField erwartet True oder False und darf standardmäßig
# keinen leeren Wert (NULL) enthalten.


# Eine Möglichkeit ist deshalb, direkt in unserem Model einen Default-Wert
# für das Field festzulegen:

    newsletter_abo = models.BooleanField(default=True)


# Dadurch bekommt das Field standardmäßig den Wert True, wenn beim
# Erstellen eines Customer kein anderer Wert angegeben wird.

# Außerdem kann Django bei der Migration den benötigten Wert für die
# bereits vorhandenen Datensätze setzen.


# Nun können wir erneut die Migration erstellen:

    python manage.py makemigrations


# Diesmal kann Django die Migration erstellen.

# Anschließend wenden wir die Migration auf unsere Datenbank an:

    python manage.py migrate


# Die Tabelle sales_customer besitzt danach zusätzlich die neue Spalte:

    newsletter_abo


# Kurz zusammengefasst:

# Neues Field ohne Default + bestehende Datensätze
#       -> Django benötigt einen Wert für die vorhandenen Datensätze

# default=True
#       -> Legt True als Standardwert für das Field fest

# python manage.py makemigrations
#       -> Erstellt die neue Migration

# python manage.py migrate
#       -> Wendet die Migration auf die Datenbank an


# default=True ist somit eine Möglichkeit, das Problem beim Hinzufügen
# eines neuen, nicht-nullbaren Fields zu bestehenden Datensätzen zu lösen.





# --------------- 10 - null und blank ----------------- #


# Doku:
# https://docs.djangoproject.com/en/6.1/ref/models/fields/


# Bei unseren Model Fields können wir unter anderem null und blank verwenden.

# Beide erlauben auf unterschiedliche Weise, dass ein Wert nicht angegeben wird.
# Dabei haben null und blank aber unterschiedliche Aufgaben.


# ---------------- null ---------------- #


# null bezieht sich auf die Speicherung in der Datenbank.

# Bei:

    null=True

# darf die Datenbank für dieses Field den Wert NULL speichern.

# NULL bedeutet, dass kein Wert vorhanden ist.


# Bei CharField und TextField sollte null=True normalerweise vermieden werden.

# Der Grund:
# Bei Textfeldern hätten wir sonst zwei Möglichkeiten für "kein Wert":

    NULL
    ""

# "" ist ein leerer String.

# Bei CharField und TextField wird deshalb normalerweise ein leerer
# String verwendet und nicht NULL.


# ---------------- blank ---------------- #


# blank bezieht sich hauptsächlich auf die Validierung eines Fields.

# Standardmäßig gilt:

    blank=False

# Das bedeutet, dass bei der Validierung ein Wert angegeben werden muss.


# Mit:

    blank=True

# erlauben wir, dass das Field bei der Validierung leer bleiben darf.


# ---------------- EmailField ---------------- #


# Nun kommentieren wir unser email_address Field wieder ein.

# Da EmailField auf einem CharField basiert, verwenden wir hier
# keinen NULL-Wert, sondern einen leeren String als Default:

    email_address = models.EmailField(
        max_length=30,
        blank=True,
        default=""
    )


# blank=True bedeutet:
# Das Field darf bei der Validierung leer bleiben.

# default="" bedeutet:
# Wird keine E-Mail-Adresse angegeben, wird ein leerer String verwendet.


# ---------------- FloatField ---------------- #


# Auch unser account Field kommentieren wir wieder ein:

    account = models.FloatField(
        blank=True,
        null=True
    )


# Hier können wir null=True verwenden, da es sich nicht um ein Textfeld handelt.

# blank=True
# -> Das Field darf bei der Validierung leer bleiben.

# null=True
# -> In der Datenbank darf NULL gespeichert werden.


# ---------------- Migration ---------------- #


# Nachdem wir die Fields wieder hinzugefügt bzw. verändert haben,
# erstellen wir eine neue Migration:

    python manage.py makemigrations


# Anschließend wenden wir die Migration auf die Datenbank an:

    python manage.py migrate


# Die neuen Fields befinden sich danach in unserer Datenbank.

# Bei unseren bereits vorhandenen Customer können diese Felder leer sein,
# da wir dies entsprechend über blank, null bzw. default erlaubt haben.


# ---------------- Kurz zusammengefasst ---------------- #


# null=True
# -> Die Datenbank darf NULL speichern.

# blank=True
# -> Das Field darf bei der Validierung leer bleiben.

# default=""
# -> Verwendet einen leeren String als Standardwert.

# CharField / TextField
# -> normalerweise lieber "" statt NULL für einen fehlenden Textwert.

# FloatField und andere Nicht-Textfelder
# -> können beispielsweise mit null=True NULL in der Datenbank erlauben.


# Merksatz:

# null  -> Datenbank
# blank -> Validierung 



# Sektion 1 Done
