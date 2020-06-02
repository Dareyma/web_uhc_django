from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.core.paginator import Paginator
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_list_or_404, get_object_or_404, render

from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout


# Login, loguot, register

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)

    return HttpResponseRedirect('/login/')


# Vistas basadas en funciones

def temporadas(request):

    temporadas = Temporada.objects.order_by('-ano')
        
    paginator = Paginator(temporadas, 8)
    page = request.GET.get('page')
    temporadas = paginator.get_page(page)

    return render(request, 'gestion/read/temporadas.html', {'temporadas': temporadas})

def temporada(request, id):
    temporadas = get_object_or_404(Temporada, id = id)
    partidas = Partida.objects.filter(temporada = temporadas)
    context={
        'temporadas': temporadas,
        'partidas': partidas,
        }
    return render(request, 'gestion/read/temporada.html', context)


def juego(request, id):
    partidas = get_object_or_404(Partida, id = id)
    equipos = Juega.objects.filter(partida = partidas)
    context={
        'equipos': equipos,
        'partidas': partidas,
        }
    return render(request, 'gestion/read/datos_partida.html', context)

def crearPartida(request):
    if request.method == 'POST':
        partida_form = PartidaForm(request.POST)

        if partida_form.is_valid():
            partida_form.save()
            return redirect('gestion:partidas')
    
    else:
        partida_form = PartidaForm()
    
    return render(request, 'gestion/create_edit/partida.html', {'partida_form': partida_form})

def editarPartida(request, id):
    partida_form = None
    error = None

    try:
        partida = Partida.objects.get(id = id)

        if request.method == 'GET':
            partida_form = PartidaForm(instance = partida)

        else:
            partida_form = PartidaForm(request.POST, instance = partida)

            if partida_form.is_valid():
                partida_form.save()
                
            return redirect('gestion:partidas')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'gestion/create_edit/partida.html', {'partida_form': partida_form, 'error': error})

def eliminarPartida(request, id):
    partida = Partida.objects.get(id = id)
    partida.delete()
    
    return redirect('gestion:partidas')

def eliminarTemporada(request, id):
    temporada = Temporada.objects.get(id = id)
    temporada.delete()
    
    return redirect('gestion:temporadas')

def eliminarEquipo(request, id):
    equipo = Juega.objects.get(id = id)
    print("Va bien")
    id_partida = equipo.partida.id

    print(id_partida)

    equipo.delete()
    
    partidas = get_object_or_404(Partida, id = id_partidas)
    equipos = Juega.objects.filter(partida = partidas)
    context={
        'equipos': equipos,
        'partidas': partidas,
        }
    return render(request, 'gestion/read/datos_partida.html', context)
    
    # return redirect('gestion:partida')


# Vistas basadas en clases

class Inicio(TemplateView):
    template_name = 'index.html'

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

class Partidas(TemplateView):
    template_name = 'gestion/read/partidas.html'

    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        partidas = Partida.objects.all()
        # nombre = partidas.

        if queryset:
            partidas = Partida.objects.filter(nombre = queryset)
            
        paginator = Paginator(partidas, 5)
        page = request.GET.get('page')
        partidas = paginator.get_page(page)

        return render(request, self.template_name, {'partidas': partidas})

class CrearJuego(CreateView):
    model = Juega
    form_class = JuegoForm

class ActualizarJuego(UpdateView):
    model = Juega
    template_name = 'gestion/create_edit/juego.html'
    form_class = JuegoForm
    success_url = reverse_lazy('gestion:partidas')

# class EliminarJuego(DeleteView):
#     model = Juega
#     success_url = 'gestion:partidas'

# class EliminarTemporada(DeleteView):
#     model = Temporada
#     success_url = 'gestion:temporadas'

class TemporadaCreateView(CreateView):
    model = Temporada
    form_class = TemporadaForm
    template_name = 'gestion/create_edit/temporada.html'
    success_url = reverse_lazy('gestion:temporadas')


