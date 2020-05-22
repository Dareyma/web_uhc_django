from django.urls import path
from .views import *


urlpatterns = [
    path('temporadas', temporadas, name='temporadas'),
    path('temporada/<int:pk>', EliminarTemporada.as_view(), name='eliminar_temporada'),
    path('temporada/<int:id>', temporada, name='temporada'),

    path('jugadores', Jugadores.as_view(), name='jugadores'),

    path('partidas', Partidas.as_view(), name='partidas'),
    path('partida/crear', crearPartida, name='crear_partida'),
    path('partida_edit/<int:id>', editarPartida, name='edit_partida'),
    path('partida/delete/<int:id>', eliminarPartida, name='eliminar_partida'),

    path('partida/<int:id>', juego, name='partida'),
    path('partida/editar/<int:pk>', ActualizarJuego.as_view(), name='editar_juego'),
]