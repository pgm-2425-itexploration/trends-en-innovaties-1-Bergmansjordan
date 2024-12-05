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
    path('detail/', views.detail, name='detail'),  # Detailpagina
    path('user/', views.user_page, name='user_page'),  # Beveiligde gebruikerspagina
    path('signup/', views.signup, name='signup'),
]
