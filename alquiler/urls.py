from unicodedata import name
from django.urls import path
from .views import HomeView,ContactPage,UbicacionPage, AddCanchaView,CanchasView,EditCanchaView,DeleteCanchaView,ReservasView,ReservasHechasView,ReservarCanchaView,ReservaCanchaConfirmadaView
from . import views

urlpatterns = [
#    path('', views.index, name = "home"),
    path('',HomeView.as_view(), name="home"),
    path('contact/', ContactPage, name="contact"),
    path('ubicacion/', UbicacionPage, name="ubicacion"),
    path('agregar_cancha/', AddCanchaView.as_view(), name="agregar_cancha"),
    path('canchas/', CanchasView.as_view(), name="canchas"),
    path('canchas/editar_cancha/<int:pk>', EditCanchaView.as_view(), name="editar_cancha"),
    path('canchas/borrar_cancha/<int:pk>', DeleteCanchaView.as_view(), name="borrar_cancha"),
    path('reservas/', ReservasView.as_view(), name="reservas"),
    path('reservas_hechas/<int:pag>', ReservasHechasView.as_view(), name="reservas_hechas"),
    path('reservar_cancha/<int:idcancha>/<int:idhora>',ReservarCanchaView.as_view(), name="reservar_cancha"),
    path('reserva_confirmada',ReservaCanchaConfirmadaView,name="reserva_confirmada")
]

