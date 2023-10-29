from django import forms
from .models import Ability, Course, Contenido


class ContenidoForm(forms.ModelForm):
    field_order = ('titulo', 'descripcion', 'content', 'abilities', 'curses')

    class Meta:
        model = Contenido
        fields = '__all__'

    titulo = forms.CharField(
        label="Título",
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width: 100%;'}
        )
    )

    descripcion = forms.CharField(
        label="Descripción",
        max_length=250,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width: 100%;'}
        )
    )

    content = forms.FileField(
        label="Archivo",
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control', 'style': 'width: 100%;'}
        )
    )

    abilities = forms.ModelMultipleChoiceField(
        queryset=Ability.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    curses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )