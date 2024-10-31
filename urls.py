from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('code_snippets/', views.code_snippets, name='code_snippets'),
    path('resources/', views.resources, name='resources'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
