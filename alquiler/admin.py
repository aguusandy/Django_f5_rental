from django.contrib import admin
from alquiler.models import Cancha,Reserva,Horario

# Register your models here.
@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    pass

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    pass

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    pass