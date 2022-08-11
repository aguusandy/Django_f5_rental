from email.policy import default
from unicodedata import name
from django import forms
from requests import request
from .models import Cancha, Horario, Reserva, User
from datetime import datetime

#forma del modelo del posteo
class CanchaForm(forms.ModelForm):
    class Meta:
        capacidad_opciones = [('Futbol 5','Futbol 5'), ('Futbol 7','Futbol 7'),]
        model = Cancha
        fields = ('nombre','capacidad','habilitada','creador','piso','techada','iluminacion')
        widgets = {
             'nombre':forms.TextInput(attrs={'class':'form-control'}),
             'capacidad':forms.Select(attrs={'class':'form-control'}, choices=capacidad_opciones),
             'piso':forms.TextInput(attrs={'class':'form-control'}),
             'creador':forms.Select(attrs={'class':'form-control'}),
            }

class EditCanchaForm(forms.ModelForm):
    class Meta:
        capacidad_opciones = [('Futbol 5','Futbol 5'), ('Futbol 7','Futbol 7'),]
        model = Cancha
        fields = ('nombre','capacidad','habilitada','creador','piso','techada','iluminacion')
        widgets = {
             'nombre':forms.TextInput(attrs={'class':'form-control'}),
             'capacidad':forms.Select(attrs={'class':'form-control'}, choices=capacidad_opciones),
             'piso':forms.TextInput(attrs={'class':'form-control'}),
             'creador':forms.Select(attrs={'class':'form-control'}),
            }

class ReservaForm(forms.ModelForm):
   
    class Meta:
        model = Reserva
        fields = ('nombre','telefono','cancha','horario')
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'cancha':forms.Select(attrs={'class':'form-control'}),
            'horario':forms.Select(attrs={'class':'form-control'}),
        }