from django.db import models

# Create your models here.
class Turno(models.Model):
    codigo = models.CharField(max_length=255)
    fecha=models.DateField()