### -------- BACKEND 6 - Django Datenbank und Adminpane ---------------- ###

## --------------- Sektion 3: Adminpanes --------------------##

# ------------ 01 - createsuperuser -------------- #


# Virtuelle Umgebung starten:

    env\Scripts\activate


# Server starten:

    python manage.py runserver


# Django Adminpanel aufrufen:

    http://127.0.0.1:8000/admin/


# Um uns einloggen zu können, erstellen wir einen Superuser:

    python manage.py createsuperuser


# Anschließend werden die Daten abgefragt:

# Username
# E-Mail-Adresse
# Passwort


# Danach können wir das Adminpanel erneut aufrufen:

    http://127.0.0.1:8000/admin/


# Dort melden wir uns mit den Daten des Superusers an.

# Im Adminpanel sehen wir zunächst unter anderem:

# Groups
# Users


# Der Superuser besitzt die benötigten Admin-Rechte,
# um das Django Adminpanel zu verwalten.




# -----------   02 - Model adminpanel registrieren ------------ #


# Damit unsere Models im Django Adminpanel angezeigt werden,
# müssen wir sie in der admin.py registrieren.

from django.contrib import admin
from .models import Customer, Product, Bill, Order, Producttype


# Models im Adminpanel registrieren:

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Producttype)


# Danach können wir die Models im Adminpanel aufrufen und verwalten.

# Beispiel Customer:
# http://127.0.0.1:8000/admin/sales/customer/


# Über das Adminpanel können wir Datensätze erstellen,
# bearbeiten und löschen.

# Änderungen werden direkt in unserer db.sqlite3 gespeichert.




# ------------ 03 - list_filter und list_display -------------- #


# Für Customer erstellen wir eine eigene Admin-Klasse,
# die von admin.ModelAdmin erbt.

# Dadurch können wir die Darstellung im Adminpanel anpassen.

class CustomerAdmin(admin.ModelAdmin):

    # list_filter erstellt rechts im Adminpanel Filtermöglichkeiten.

    list_filter = ['first_name', 'last_name']

    # list_display bestimmt, welche Spalten in der
    # Tabellenansicht angezeigt werden.

    list_display = ['last_name', 'account']


# Anschließend registrieren wir Customer mit unserer Admin-Klasse.

admin.site.register(Customer, CustomerAdmin)





# ------------ 04 - fields und fieldsets -------------- #


# Mit fields und fieldsets können wir die Eingabefelder
# beim Hinzufügen oder Bearbeiten im Adminpanel anpassen.

# Doku:
# https://docs.djangoproject.com/en/6.1/ref/contrib/admin/


# fields bestimmt, welche Eingabefelder angezeigt werden:

# fields = ['first_name', 'last_name', 'account']


# Mit fieldsets können wir die Felder zusätzlich gruppieren
# und Bereiche ein- und ausklappbar machen.

class CustomerAdmin(admin.ModelAdmin):

    list_filter = ['first_name', 'last_name']
    list_display = ['last_name', 'account']

    fieldsets = [
        (
            None,
            {
                'fields': ['first_name', 'last_name', 'account'],
            },
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse'],
                'fields': ['newsletter_abo'],
            },
        ),
    ]


# "collapse" macht den Bereich "Advanced options"
# im Adminpanel ein- und ausklappbar.





# ------   05 - model Meta class (verbosename und ordering) -------- #




# In der models.py können wir über die Meta-Klasse
# zusätzliche Einstellungen für unser Model festlegen.

class Meta:
    verbose_name = 'Customer'
    verbose_name_plural = 'Customers'
    ordering = ['-first_name']


# verbose_name bestimmt den Namen eines einzelnen Objekts.
# verbose_name_plural bestimmt den Namen in der Mehrzahl.

# ordering bestimmt die Standardsortierung.
# Das "-" vor first_name bedeutet absteigend.


# Mit __str__ bestimmen wir, wie einzelne Customer-Objekte
# lesbar dargestellt werden.

def __str__(self):
    return f"{self.first_name} {self.last_name}"


# Dadurch sehen wir z.B. in der Shell und im Adminpanel:

# John Doe
# Jane Smith

# statt:

# Customer object (1)
# Customer object (2)


# Meta und __str__ werden direkt im jeweiligen Model
# in der models.py definiert.






# --------- 06 - readonly_fields und save() überschreiben ----------- #


# Im Adminpanel können wir Felder als readonly festlegen.
# Diese Felder können dann angezeigt, aber nicht bearbeitet werden.

# Beispiel:
# Eine Background Color für ein User-Profil soll automatisch
# generiert werden und nicht vom User eingetragen werden.


# models.py

# Mit save() können wir die normale save-Methode überschreiben
# und vor dem Speichern eigene Aktionen durchführen.

def save(self, *args, **kwargs):
    self.account = 651681
    return super().save(*args, **kwargs)


# In unserem Beispiel wird account beim Speichern
# automatisch auf 651681 gesetzt.


# admin.py

# readonly_fields verhindert, dass account im Adminpanel
# vom User verändert werden kann.

readonly_fields = ['account']


# Kurz:
# readonly_fields -> Feld anzeigen, aber nicht bearbeiten
# save()          -> eigene Logik beim Speichern ausführen




# ------------ 07 - prepopulated_fields und SlugField -------------- #


# models.py

# Mit SlugField können wir einen URL-freundlichen Wert speichern.

class Customer(models.Model):
    slug = models.SlugField(blank=True, default="")


# admin.py

# Mit prepopulated_fields wird das Slug-Feld automatisch
# aus first_name und last_name vorausgefüllt und slugify angewendet.

class CustomerAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ['first_name', 'last_name']
    }


# Das slug-Feld nehmen wir zusätzlich in die Advanced options auf.

    fieldsets = [
        (
            None,
            {
                'fields': ['first_name', 'last_name', 'account'],
            },
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse'],
                'fields': ['newsletter_abo', 'slug'],
            },
        ),
    ]


# Beispiel:

# first_name: Pascal
# last_name:  Weinberg

# Daraus wird automatisch:

# slug: pascal-weinberg


# Slugs eignen sich besonders für lesbare und URL-freundliche Pfade.





# ------------ 08 - Field Options und help_text -------------- #


# Doku:
# https://docs.djangoproject.com/en/6.1/ref/models/fields/


# Über Field Options können wir das Verhalten unserer
# Model-Felder weiter anpassen.

class Customer(models.Model):

    first_name = models.CharField(
        max_length=30,
        help_text='max 30 letters, dummy'
    )


# help_text wird als zusätzlicher Hinweis zum Eingabefeld
# angezeigt, z.B. auch im Adminpanel.


# Für eigene Fehlermeldungen gibt es error_messages.
# Diese können z.B. bei einer fehlgeschlagenen Validierung
# angezeigt werden.


# Kurz:
# help_text      -> Hinweis für den User
# error_messages -> eigene Fehlermeldungen





#                              Sektion 3 Done