from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=255)
    apellido= models.CharField(max_length=255)
    dni = models.CharField(max_length=8)