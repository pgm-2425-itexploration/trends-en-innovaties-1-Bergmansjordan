from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Berichten

admin.site.register(Berichten)
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')
