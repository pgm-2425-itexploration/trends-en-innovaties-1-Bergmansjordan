
# Django Tutorial voor Beginners

Django is een krachtig en populair webframework voor Python dat veel wordt gebruikt voor het bouwen van robuuste en schaalbare webapplicaties. In deze tutorial leer je de basisprincipes van Django en bouw je een eenvoudige webapplicatie.

## Stap 1: Installeren van Django

### Voorbereiding
Om met Django te werken, moet Python geïnstalleerd zijn op je systeem. Je kunt dit controleren door het volgende commando in je terminal of command prompt te typen:

```bash
python --version
```
Zorg ervoor dat je Python 3.6 of hoger hebt.

### Django Installeren
Je kunt Django eenvoudig installeren met pip (de Python package manager). Voer het volgende commando uit:

```bash
pip install django
```

Zodra Django is geïnstalleerd, kun je de installatie controleren door het versienummer te controleren:

```bash
django-admin --version
```

## Stap 2: Een Django Project Maken

### Een nieuw project aanmaken
In Django begint alles met een project. Dit project is een verzameling van instellingen voor je website. Maak een nieuwe directory aan waar je je project wilt opslaan en voer het volgende commando uit:

```bash
django-admin startproject mijnproject
```

Dit creëert een nieuwe directory genaamd `mijnproject` met de volgende structuur:

```
mijnproject/
    manage.py
    mijnproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### Uitleg over de bestanden:
- **manage.py**: Een command-line utility waarmee je verschillende Django-beheertaken kunt uitvoeren.
- **settings.py**: Hierin staan alle instellingen voor je Django project.
- **urls.py**: Hierin definieer je de URL's en routes van je project.
- **wsgi.py/asgi.py**: Deze bestanden helpen bij het deployen van je project.

## Stap 3: De Django Development Server Starten

Ga naar de directory van je project en start de ontwikkelserver:

```bash
cd mijnproject
python manage.py runserver
```

Je zou nu een bericht moeten zien dat de server draait op `http://127.0.0.1:8000/`. Open je webbrowser en ga naar dat adres om de standaard Django-welkomstpagina te zien.

## Stap 4: Een Django App Maken

In Django bestaat een project uit meerdere apps. Een app is een webcomponent die een specifieke functionaliteit biedt (zoals een blog of een winkelmandje).

Maak een nieuwe app binnen je project door het volgende commando uit te voeren:

```bash
python manage.py startapp mijnapp
```

Dit creëert een nieuwe map `mijnapp` in je project met de volgende structuur:

```
mijnapp/
    __init__.py
    admin.py
    apps.py
    models.py
    views.py
    tests.py
```

### Uitleg over de bestanden:
- **models.py**: Hierin definieer je de datamodellen (database schema’s).
- **views.py**: Hierin definieer je de logica voor wat de gebruiker te zien krijgt.
- **admin.py**: Hierin beheer je hoe je modellen zichtbaar zijn in het Django admin paneel.
- **tests.py**: Hier kun je tests schrijven om je app te testen.

## Stap 5: Een Eenvoudige View Maken

Laten we nu een eenvoudige view maken die "Hallo, wereld!" weergeeft wanneer we een specifieke URL bezoeken.

1. Open `views.py` in je `mijnapp` map en voeg de volgende code toe:

    ```python
    from django.http import HttpResponse

    def hallo_wereld(request):
        return HttpResponse("Hallo, wereld!")
    ```

2. Voeg nu een URL toe die naar deze view verwijst. Maak een bestand `urls.py` aan in de map `mijnapp` (dit bestaat nog niet) met de volgende inhoud:

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.hallo_wereld, name='hallo_wereld'),
    ]
    ```

3. Om ervoor te zorgen dat deze URL toegankelijk is, moeten we de app-URL’s aan het project-URL-bestand koppelen. Open het bestand `urls.py` in de hoofdmap `mijnproject` en voeg deze code toe:

    ```python
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('mijnapp.urls')),  # Verbindt mijnapp.urls
    ]
    ```

## Stap 6: Database Instellen en Modellen Maken

Django gebruikt standaard SQLite als database. Om je database te initialiseren, voer je dit commando uit:

```bash
python manage.py migrate
```

### Een model toevoegen
Laten we nu een eenvoudig datamodel maken. Open `models.py` in de map `mijnapp` en voeg het volgende toe:

```python
from django.db import models

class Berichten(models.Model):
    titel = models.CharField(max_length=100)
    inhoud = models.TextField()

    def __str__(self):
        return self.titel
```

Voer daarna het volgende commando uit om de wijzigingen aan te brengen in de database:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Stap 7: Werken met de Django Admin

Om toegang te krijgen tot het admin dashboard van Django, moeten we het model registreren in `admin.py`. Open `admin.py` en voeg het volgende toe:

```python
from django.contrib import admin
from .models import Berichten

admin.site.register(Berichten)
```

Maak nu een superuser account aan voor de admin-interface:

```bash
python manage.py createsuperuser
```

Voer je gebruikersnaam, e-mailadres en wachtwoord in.

Start de server opnieuw:

```bash
python manage.py runserver
```

Ga naar `http://127.0.0.1:8000/admin` en log in met je superusergegevens. Je kunt nu het `Berichten` model beheren via de admin interface.

## Stap 8: Templates Gebruiken

Django maakt gebruik van templates voor het weergeven van HTML. Laten we een eenvoudige template toevoegen voor onze "Hallo, wereld!" pagina.

1. Maak een directory aan genaamd `templates` in de map `mijnapp`.
2. Maak in deze directory een bestand genaamd `index.html` en voeg de volgende inhoud toe:

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hallo Wereld</title>
    </head>
    <body>
        <h1>{{ bericht }}</h1>
    </body>
    </html>
    ```

3. Pas je view in `views.py` aan om een template te gebruiken:

    ```python
    from django.shortcuts import render

    def hallo_wereld(request):
        context = {
            'bericht': 'Hallo, wereld!'
        }
        return render(request, 'index.html', context)
    ```

Nu wordt de "Hallo, wereld!" boodschap weergegeven via een template.

## Stap 9: De Django App Verfijnen en Uitbreiden

Nu je de basis van Django onder de knie hebt, kun je:

- Meer complexe datamodellen maken in `models.py`.
- Formulieren maken en data van gebruikers verwerken.
- Meer templates maken voor een dynamische en aantrekkelijke interface.
- Werken met externe bibliotheken en API’s.

---