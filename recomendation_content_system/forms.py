from django.forms import ModelForm, NumberInput
from django import forms
from .models import Ability, Course, Contenido


class ContentForm(forms.ModelForm):
    field_order = ('titulo', 'descripcion', 'content', 'abilities', 'curses')

    class Meta:
        model = Contenido
        fields = '__all__'
        labels = {
            'titulo': 'Título',
            'content': 'Archivo',
            'abilities': 'Habilidades',
            'curses': 'Cursos',
            'descripcion': 'Descripción',
        }