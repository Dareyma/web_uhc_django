from django.urls import path
from .views import *

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('temporadas', login_required(temporadas), name='temporadas'),
    path('temporada/delete/<int:id>', eliminarTemporada, name='eliminar_temporada'),
    path('temporada/<int:id>', temporada, name='temporada'),
    path('temporada/add', TemporadaCreateView, name='add_temporada'),

    path('jugadores', Jugadores.as_view(), name='jugadores'),

    path('partidas', login_required(Partidas.as_view()), name='partidas'),
    path('partida/crear', crearPartida, name='crear_partida'),
    path('partida_edit/<int:id>', editarPartida, name='edit_partida'),
    path('partida/delete/<int:id>', eliminarPartida, name='eliminar_partida'),

    path('partida/<int:id>', juego, name='partida'),
    path('partida/editar/<int:pk>', ActualizarJuego.as_view(), name='editar_juego'),

    path('equipo/delete/<int:id>', eliminarEquipo, name='eliminar_equipo'),
]