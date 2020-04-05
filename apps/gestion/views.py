from django.shortcuts import render
from .models import *

from django.core.paginator import Paginator
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView

# Vistas basadas en funciones

def temporada(request):

    temporadas = Temporada.objects.order_by('ano')
        
    paginator = Paginator(temporada, 8)
    page = request.GET.get('page')
    temporada = paginator.get_page(page)

    return render(request, 'gestion/read/temporada.html', {'temporadas': temporadas})

# Vistas basadas en clases

class Jugadores(TemplateView):
    template_name = 'gestion/read/jugadores.html'

    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        jugadores = Jugador.objects.order_by('-victorias')

        if queryset:
            jugadores = Jugador.objects.filter(nombre = queryset)
            
        paginator = Paginator(jugadores, 5)
        page = request.GET.get('page')
        jugadores = paginator.get_page(page)

        return render(request, self.template_name, {'jugadores': jugadores, 'numero': 1})
