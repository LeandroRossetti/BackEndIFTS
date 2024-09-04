from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255, validators=[MinLengthValidator(8)])
    email = models.EmailField(validators=[EmailValidator()])
    nivel = models.CharField(
        max_length=50,
        choices=[('admin', 'Admin'), ('staff', 'Staff')],
        default='staff'
    )

    def __str__(self):
        return self.nombre
