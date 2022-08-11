from dataclasses import Field
from datetime import datetime
from operator import index
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Horario(models.Model):
    id = models.AutoField(primary_key=True,auto_created = True, serialize = False)
    #solo pueden haber horas en las que este abierto el lugar
    hora = models.IntegerField(null=False, blank=False)


class Cancha(models.Model):
    id = models.AutoField(primary_key=True,auto_created = True, serialize = False)
    #nombre de la cancha
    nombre = models.CharField(max_length=255, null=False, blank=False)
    #capacidad si es de futbol 5 o futbol 7
    capacidad = models.CharField(max_length=255, null=False, blank=False)
    #esta habilitada?
    habilitada = models.BooleanField(default=True)
    #quien creo o edito la cancha
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    #tipo de piso
    piso = models.CharField(max_length=255, null=False, blank=False, default="sintetico")
    #esta techada
    techada = models.BooleanField(default=True)
    #tiene iluminacion
    iluminacion = models.BooleanField(default=True)

    def horarios_disponible(self):
        fecha_actual = datetime.now().date()
        horarios = Horario.objects.all()
        reservas = Reserva.objects.all().filter(fecha = fecha_actual)
        horarios_disponibles = []

        for hor in horarios:
            horarios_disponibles.append(hor)

        for reserva in reservas:
            if(self.id == reserva.cancha.id):
               horarios_disponibles.remove(reserva.horario)
        
        return horarios_disponibles

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('home')

class Reserva(models.Model):
    id = models.AutoField(primary_key=True,auto_created = True, serialize = False)
    #nombre de quien crea la reserva
    nombre = models.CharField(max_length=255, null=False, blank=False)
    #numero telefono para contacto
    telefono = models.CharField(max_length=255, null=False, blank=False)
    #cancha elegida para crear la reserva
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    #fecha de la reserva
    fecha = models.DateField(auto_now_add=True)
    #horario
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.nombre