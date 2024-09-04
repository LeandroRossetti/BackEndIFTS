from django.db import models

# Create your models here.
class Salon(models.Model):
    nombre = models.CharField(max_length=255)
    capacidad=models.IntegerField