from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

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