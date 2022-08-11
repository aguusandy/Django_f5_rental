
from urllib import request
from django import http
from django.views import View
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reserva, Cancha, Horario
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import CanchaForm,EditCanchaForm,ReservaForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    #tipo de modelo
    model = Cancha
    #nombre de la plantilla
    template_name = 'home.html'

class ReservasView(ListView):
    #tipo de modelo
    model = Reserva
    #nombre de la plantilla
    template_name = 'reservas.html'
    #ordering = ['-post_date','-id']
    def get_context_data(self, *args, **kwargs):
        canchas = Cancha.objects.all()
        info = []
        for cancha in canchas:
            horarios_disponibles = cancha.horarios_disponible()
            
            

            inf = [ cancha , horarios_disponibles ]
            info.append(inf)
            horarios_disponibles = []
        context = super(ReservasView, self).get_context_data(*args, **kwargs)
        context["info"] = info
        return context

class AddCanchaView(CreateView):
    #modelo de la clase 
    model = Cancha
    #formas de que tomará el formulario
    form_class = CanchaForm
    template_name = 'agregar_cancha.html'
    success_url = reverse_lazy('canchas')

class CanchasView(ListView):
    model = Cancha
    template_name = 'cancha.html'
    def get_context_data(self, *args, **kwargs):
        canchas = Cancha.objects.all()
        context = super(CanchasView, self).get_context_data(*args, **kwargs)
        context["canchas"] = canchas
        return context

class EditCanchaView(UpdateView):
    model = Cancha
    form_class = EditCanchaForm
    template_name = 'editar_cancha.html'
    success_url = reverse_lazy('canchas')

class DeleteCanchaView(DeleteView):
    model = Cancha
    template_name = 'borrar_cancha.html'
    success_url = reverse_lazy('canchas')


class DeleteCanchaView(DeleteView):    
    model = Cancha
    template_name = 'borrar_cancha.html'


def UbicacionPage(request):
    return render(request, 'ubicacion.html')


def ContactPage(request):

    if request.method == "POST":
        nombre_contacto = request.POST['nombre']
        email_contacto = request.POST['email']
        mensaje_contacto = request.POST['mensaje']
        
        #enviar email
        send_mail(
            "Mensaje de " + nombre_contacto,
            mensaje_contacto + email_contacto,
            email_contacto,
            ['emailF5@gmail.com'],
            fail_silently=False,           
        )
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

class ReservasHechasView(ListView):
    #tipo de modelo
    model = Reserva
    #nombre de la plantilla
    template_name = 'reservas_hechas.html'

    def get_context_data(self, *args, **kwargs):
        reservas = Reserva.objects.all().order_by('-id')
        context = super(ReservasHechasView, self).get_context_data(*args, **kwargs)
        context["reservas"] = reservas
        return context

class ReservarCanchaView(CreateView):
    
    #modelo de la clase 
    model = Reserva
    #formas de que tomará el formulario
    form_class = ReservaForm
    template_name = 'reservar_cancha.html'
    def get_context_data(self, *args, **kwargs):
        canchas = Cancha.objects.all()
        horarios = Horario.objects.all()
        context = super(ReservarCanchaView, self).get_context_data(*args, **kwargs)
        context["canchas"] = canchas
        context["horarios"] = horarios
        return context

    success_url = reverse_lazy('reserva_confirmada')
    

def ReservaCanchaConfirmadaView(request):
    return render(request,'reserva_confirmada.html')
    
def error_404_view(request,exception):
    return render(request,'not_found_page.html')