### -------- BACKEND 6 - Django Datenbank und Adminpane ---------------- ###

# --------------- Sektion 5: Views & Aufgabe -------------------- #


# ------------------- 01 - Einführung ------------------------- #


# Bevor wir mit dem eigenen Projekt starten, schauen wir uns
# die eingebauten Class-Based Generic Views von Django an.

# Diese Views können uns Arbeit abnehmen, wenn wir z.B.
# Daten schnell aus der Datenbank anzeigen möchten.

# Doku:
# https://docs.djangoproject.com/en/6.1/topics/class-based-views/generic-display/


# Zuerst erweitern wir die globale urls.py unseres Projekts:

from django.urls import include, path

urlpatterns = [
    path('sales/', include('sales.urls')),
]


# Dadurch werden alle URLs unter /sales/
# an unsere sales App weitergeleitet.


# Anschließend erstellen wir im App-Ordner sales
# eine eigene urls.py:

from django.urls import path


urlpatterns = [

]


# Hier werden wir anschließend die einzelnen URLs
# unserer sales App definieren.




# ------------------- 02 - ListView (Einstieg) ------------------------- #


# Doku:
# https://docs.djangoproject.com/en/6.1/ref/class-based-views/generic-display/


# Mit einer ListView können wir mehrere Objekte eines Models
# aus der Datenbank abrufen und in einem Template anzeigen.


# 1. App in settings.py prüfen
# --------------------------------------------------

# Zuerst prüfen wir, ob unsere App "sales" bereits
# unter INSTALLED_APPS registriert ist.

INSTALLED_APPS = [
    ...
    'sales',
]


# 2. Template-Ordner erstellen
# --------------------------------------------------

# In unserer sales App erstellen wir folgende Ordnerstruktur:

# sales/
# ├── templates/
# │   └── sales/
# │       └── list.html
# ├── urls.py
# ├── views.py
# └── models.py


# 3. list.html erstellen
# --------------------------------------------------

# In sales/templates/sales/list.html:

"""
<ul>
    {% for customer in object_list %}
        <li>{{ customer.first_name }}</li>
    {% empty %}
        <li>No customers yet.</li>
    {% endfor %}
</ul>
"""

# object_list wird von der ListView automatisch
# an unser Template übergeben.


# 4. ListView in views.py erstellen
# --------------------------------------------------

# Zuerst importieren wir ListView und unser Customer Model:

from django.views.generic.list import ListView
from .models import Customer


# Danach erstellen wir unsere View:

class CustomerListView(ListView):
    model = Customer
    template_name = 'sales/list.html'


# Unsere CustomerListView erbt von der Django ListView.

# Mit model = Customer legen wir fest,
# welche Objekte aus der Datenbank angezeigt werden sollen.

# template_name legt fest, welches Template verwendet wird.


# 5. View in sales/urls.py importieren
# --------------------------------------------------

from django.urls import path
from .views import CustomerListView


# Danach verbinden wir die View mit einer URL:

urlpatterns = [
    path('', CustomerListView.as_view()),
]


# .as_view() macht unsere Class-Based View für das
# Django URL-System verwendbar.


# 6. Globale urls.py
# --------------------------------------------------

# In database_project/urls.py haben wir bereits:

from django.urls import include, path

urlpatterns = [
    path('sales/', include('sales.urls')),
]


# Dadurch wird unsere sales/urls.py unter /sales/ eingebunden.


# 7. Server starten
# --------------------------------------------------

    python manage.py runserver


# Anschließend im Browser öffnen:

# http://127.0.0.1:8000/sales/


# Ablauf:
#
# Browser
#    ↓
# database_project/urls.py
#    ↓
# sales/urls.py
#    ↓
# CustomerListView
#    ↓
# Customer Model / Datenbank
#    ↓
# sales/list.html
#    ↓
# Customer werden im Browser angezeigt





# ------------------- 03 - ListView (Parameter & Query) ------------------ #


# Mit paginate_by können wir festlegen, wie viele Einträge
# pro Seite von unserer ListView angezeigt werden.


# sales/views.py

class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"
    paginate_by = 2


# paginate_by = 2 bedeutet:
# Pro Seite werden maximal 2 Customer angezeigt.


# model = Customer entspricht grundsätzlich dem QuerySet:

    Customer.objects.all()


# Wir können deshalb alternativ auch schreiben:

class CustomerListView(ListView):
    queryset = Customer.objects.all()
    template_name = "sales/list.html"


# --------------------------------------------------
# Über die URL nach einem Customer filtern
# --------------------------------------------------


# Dafür erstellen wir eine zweite View, die von unserer
# CustomerListView erbt.

class CustomerListSearchView(CustomerListView):

    def get_queryset(self):
        name = self.kwargs.get("name")

        return Customer.objects.filter(
            first_name__icontains=name
        )


# get_queryset() bestimmt, welche Datensätze die ListView bekommt.

# self.kwargs enthält Parameter, die aus der URL kommen.

# Mit:
    self.kwargs.get("name")

# holen wir den Wert des URL-Parameters "name".


# first_name__icontains sucht nach Customers, deren
# first_name den eingegebenen Text enthält.

# icontains ignoriert dabei Groß- und Kleinschreibung.


# sales/urls.py

from django.urls import path
from .views import CustomerListView, CustomerListSearchView


urlpatterns = [
    path('', CustomerListView.as_view()),
    path('<str:name>/', CustomerListSearchView.as_view()),
]


# Dadurch können wir direkt über die URL filtern.


# Beispiel:

# http://127.0.0.1:8000/sales/John/

# URL:
# "John"
#   ↓
# <str:name>
#   ↓
# self.kwargs.get("name")
#   ↓
# first_name__icontains="John"
#   ↓
# Datenbank wird nach passenden Customers gefiltert


# Auch eine teilweise Eingabe funktioniert:

# http://127.0.0.1:8000/sales/jo/

# könnte z.B. "John" finden, weil __icontains
# nur prüft, ob "jo" im first_name enthalten ist.


# Kurz:
# paginate_by     -> begrenzt Einträge pro Seite
# get_queryset()  -> bestimmt / verändert das QuerySet der View
# self.kwargs     -> enthält Parameter aus der URL
# <str:name>      -> nimmt einen String aus der URL entgegen
# __icontains     -> enthält den Wert, Groß-/Kleinschreibung egal





# ------------------- 04 - DetailView (Einstieg) ------------------------- #


# Mit einer DetailView können wir einen einzelnen Datensatz
# anhand seines Primary Keys anzeigen.


# 1. DetailView in sales/views.py erstellen
# --------------------------------------------------

from django.views.generic.detail import DetailView
from .models import Customer


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "sales/detail.html"


# model = Customer legt fest, aus welchem Model
# der einzelne Datensatz geladen werden soll.


# 2. detail.html erstellen
# --------------------------------------------------

# Im Ordner:
# sales/templates/sales/detail.html

"""
<h1>{{ object.first_name }}</h1>
<p>{{ object.last_name }}</p>
"""


# object enthält den einzelnen Customer,
# den unsere DetailView aus der Datenbank geladen hat.


# 3. sales/urls.py erweitern
# --------------------------------------------------

from django.urls import path
from .views import (
    CustomerListView,
    CustomerListSearchView,
    CustomerDetailView
)


urlpatterns = [
    path('', CustomerListView.as_view()),
    path('customer/<int:pk>/', CustomerDetailView.as_view()),
]


# <int:pk> nimmt den Primary Key aus der URL entgegen.

# Beispiel:
# http://127.0.0.1:8000/sales/customer/1/

# Die DetailView sucht dadurch automatisch nach:

# Customer mit pk = 1


# Ablauf:
# /sales/customer/1/
#        ↓
# <int:pk> = 1
#        ↓
# CustomerDetailView
#        ↓
# Customer mit Primary Key 1
#        ↓
# detail.html




# ------------------- 05 - DetailView (get_object) ------------------------- #


# Bei einer DetailView können wir get_object() überschreiben,
# um das geladene Objekt zusätzlich zu bearbeiten.


# sales/views.py

from django.utils import timezone


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "sales/detail.html"


    # get_object() holt das einzelne Objekt der DetailView.

    def get_object(self):
        obj = super().get_object()

        # Wir fügen dem Objekt zusätzlich die aktuelle Zeit hinzu.

        obj.last_accessed = timezone.now()

        return obj


# last_accessed existiert hier nur auf dem Python-Objekt
# und wird dadurch nicht automatisch in der Datenbank gespeichert.


# In der detail.html können wir den Wert anschließend ausgeben:

"""
<h1>{{ object.first_name }}</h1>
<p>{{ object.last_name }}</p>
<p>{{ object.last_accessed }}</p>
"""


# Kurz:
# get_object()         -> holt das einzelne Objekt der DetailView
# super().get_object() -> nutzt die normale Logik der DetailView
# timezone.now()       -> aktuelle Zeit
# return obj           -> gibt das bearbeitete Objekt an die View zurück


#                       Modul 6 Abgeschlossen 
