from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

def features(request):
    return render(request, 'features.html')

def tutorials(request):
    return render(request, 'tutorials.html')

def code_snippets(request):
    return render(request, 'code_snippets.html')

def resources(request):
    return render(request, 'resources.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')


# Overzichtspagina met algemene informatie over Django
def overview(request):
    context = {
        'title': 'Django Overzicht',
        'content': (
            "Django is een high-level Python-webframework dat het snel en makkelijk maakt "
            "om krachtige, onderhoudbare webapplicaties te bouwen. Het volgt het "
            "Model-View-Controller (MVC)-ontwerppatroon, biedt ingebouwde beveiliging, "
            "en heeft een groot ecosysteem aan tools en plugins."
        ),
        'features': [
            "Snel ontwikkelen met minder code",
            "Sterke ingebouwde beveiliging",
            "Krachtige ORM voor databasebeheer",
            "Grote en actieve community",
        ]
    }
    return render(request, 'overview.html', context)

# Detailpagina met specifieke aspecten van Django
def detail(request):
    context = {
        'title': 'Meer details over Django',
        'sections': [
            {
                'heading': 'Beveiliging',
                'content': (
                    "Django beschermt tegen veelvoorkomende beveiligingsrisico’s zoals SQL-injecties, "
                    "Cross-Site Scripting (XSS) en Cross-Site Request Forgery (CSRF)."
                ),
            },
            {
                'heading': 'Ingebouwde Tools',
                'content': (
                    "Met de ingebouwde admin interface kun je snel data beheren zonder extra code te schrijven. "
                    "Het framework biedt ook ingebouwde ondersteuning voor gebruikersauthenticatie."
                ),
            },
            {
                'heading': 'Schaalbaarheid',
                'content': (
                    "Django kan eenvoudig worden geschaald dankzij ondersteuning voor caching, "
                    "asynchrone views en integratie met externe databases zoals PostgreSQL en MySQL."
                ),
            },
        ]
    }
    return render(request, 'detail.html', context)

# Beveiligde gebruikerspagina
@login_required
def user_page(request):
    context = {
        'title': 'Uw Gebruikerspagina',
        'message': f"Welkom, {request.user.username}! Dit is een beveiligde route.",
    }
    return render(request, 'user_page.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log automatisch in na registratie
            return redirect('user_page')  # Redirect naar gebruikerspagina
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})