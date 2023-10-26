from django.forms import ModelForm, NumberInput

from recomendation_profile_system.models import ProfessionalOffer, Settings


class ProfessionalOfferForm(ModelForm):
    field_order = ('title', 'address', 'abilities')

    class Meta:
        model = ProfessionalOffer
        fields = '__all__'


class SettingsForm(ModelForm):
    field_order = ('cant_element_to_show', 'relevance_umbral')

    class Meta:
        model = Settings
        fields = ('cant_element_to_show', 'relevance_umbral')
        widgets = {
            'cant_element_to_show': NumberInput(
                attrs={
                    'class': 'form-control select2 select2-hidden-accessible',
                    'style': 'width: 100%;',
                    'title': 'La cantidad de elementos a mostrar permite establecer un límite de resultados en el sistema de recomendación.\n'
                             'Su valor se encuentra entre 0 y 100',
                }
            ),
            'relevance_umbral': NumberInput(
                attrs={
                    'class': 'form-control select2 select2-hidden-accessible',
                    'style': 'width: 100%;',
                    'title': 'El umbral de relevancia permite establecer el grado de similitud de los resultados del sistema de recomendación.\n '
                             'Su valor se encuentra entre 0 y 100. Mientras más cercano a 100 más similares serán los resultados.',
                }
            ),
        }
