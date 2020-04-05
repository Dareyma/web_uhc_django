from django.urls import path
from .views import *


urlpatterns = [
    path('temporada', temporada, name='temporada'),
    path('jugadores', Jugadores.as_view(), name='jugadores')
]