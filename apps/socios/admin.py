from django.contrib import admin
from .models import Socio

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ['apellido']
