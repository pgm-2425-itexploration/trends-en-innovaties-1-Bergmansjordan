from django.db import models

# Create your models here.
from django.db import models

class Berichten(models.Model):
    titel = models.CharField(max_length=100)
    inhoud = models.TextField()

    def __str__(self):
        return self.titel
