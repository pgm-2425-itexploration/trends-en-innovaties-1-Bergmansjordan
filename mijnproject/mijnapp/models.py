from django.db import models

# Create your models here.
from django.db import models

class Berichten(models.Model):
    titel = models.CharField(max_length=100)
    inhoud = models.TextField()

    def __str__(self):
        return self.titel


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title