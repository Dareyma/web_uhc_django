from .models import *

from django.contrib.auth.forms import AuthenticationForm
from django import forms


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juega
        fields = ['equipo', 'jugador', 'partida' ]
        labels = {
            'equipo': 'nombre del equipo',
        }

        widgets = {
            'equipo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del equipo'
                }
            ),
            'kills': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese las kills del equipo'
                }
            ),
            'ganador': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'jugador': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'partida': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            )
        }


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ['dia', 'hora_inic', 'hora_fin', 'temporada' ]
        labels = {
            'dia': 'Día de la partida',
            'hora_init': 'Hora inicio de la partida',
            'hora_fin': 'Hora de finalización de la partida',
            'temporada': 'Temporada en la que se lleva a cabo la partida'
        }

        widgets = {
            'dia': forms.DateTimeInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'hora_init': forms.TimeInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'hora_fin': forms.TimeInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'temporada': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            )
        }