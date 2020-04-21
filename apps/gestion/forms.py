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
            'dia': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del clan'
                }
            ),
            'hora_init': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripcion del clan'
                }
            ),
            'hora_fin': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la nacionalidad del clan'
                }
            ),
            'temporada': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el tipo del clan'
                }
            )
        }