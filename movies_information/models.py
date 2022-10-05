from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Movie(models.Model):
    MovieId = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=500)
    Calificacion = models.IntegerField()
    Pais = models.CharField(max_length=500)
