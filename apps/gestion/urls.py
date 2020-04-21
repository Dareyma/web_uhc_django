from django.urls import path
from .views import *


urlpatterns = [
    path('temporadas', temporadas, name='temporadas'),
    path('temporada/<int:id>', temporada, name='temporada'),
    path('jugadores', Jugadores.as_view(), name='jugadores'),
    path('partidas', Partidas.as_view(), name='partidas'),
    path('partida/<int:id>', partida, name='partida'),
]