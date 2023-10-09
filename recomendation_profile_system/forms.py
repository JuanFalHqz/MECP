from django.forms import ModelForm

from recomendation_profile_system.models import JobOffer, Settings


class JobOfferForm(ModelForm):
    field_order = ('title', 'address', 'abilities')

    class Meta:
        model = JobOffer
        fields = '__all__'


class SettingsForm(ModelForm):
    field_order = ('cant_element_to_show', 'relevance_umbral')

    class Meta:
        model = Settings
        fields = '__all__'


