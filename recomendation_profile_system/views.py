from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView

from recomendation_profile_system.forms import SettingsForm
from recomendation_profile_system.models import ProfessionalOffer, Settings
from recomendation_profile_system.view_ import Recommendation, Url


class ListOffertProfessionalByGraduateProfile(LoginRequiredMixin, ListView):
    template_name = 'list_professional_offer_by_graduate_profile.html'
    model = ProfessionalOffer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        rpj = ProfessionalOffersRecommender(self.request.user.student)
        list = rpj.get_recommendations_by_graduate()
        context['job_offer'] = list
        context['count'] = len(context['job_offer'])

        ids = []
        for e in list:
            ids.append(e['offer'].id)
        ls = ProfessionalOffer.objects.all()
        ls = [f for f in ls if f.pk not in ids]
        context['job_offer_not_recommended'] = ls
        context['count2'] = len(ls)
        return context


class ProfessionalOffersRecommender:
    """
    Obtener las ofertas profesionales rcomendadas basado en los datos del usuario
    requiere:
        lista de ofertas profesionales
        usuario
    retorna
        lista de perfiles
    """
    professional_offers = ''
    graduate = ''
    setting = ''

    def __init__(self, student):
        self.professional_offers = ProfessionalOffer.objects.all()
        self.graduate = student
        self.setting = Settings.objects.get(user_id=student.user.settings.pk)

    def get_graduate_preferences_to_text(self):
        try:
            return self.graduate.str_meta_data()
        except Exception as e:
            e.__str__()

    def get_professional_offers_to_text(self):
        offers = []
        try:
            for job in self.professional_offers:
                offers.append({
                    'id': job.pk,
                    'meta': job.str_meta_data()
                })
            return offers
        except Exception as e:
            e.__str__()

    def get_recommendations_by_graduate(self):
        """
        Retorna una lista de ofertas de trabajo de acorde al umbral de similitud.
        """
        offers_recomendated = []
        offers = self.get_professional_offers_to_text()
        professional_profile = self.get_graduate_preferences_to_text()
        try:
            r = Recommendation()
            for offer in offers:
                similarity = r.get_similarity(professional_profile, offer['meta'])
                if similarity * 100 >= self.setting.relevance_umbral:
                    offers_recomendated.append({
                        'offer': ProfessionalOffer.objects.get(pk=offer['id']),
                        'similarity': round(similarity * 100, 2)
                    })
            # ordenar y tomar según la cantidad
            offers_recomendated.sort(key=lambda x: x['similarity'], reverse=True)
            if len(offers_recomendated) > self.setting.cant_element_to_show:
                _similarities_ = offers_recomendated
                offers_recomendated = []
                i = 0
                while i < self.setting.cant_element_to_show:
                    offers_recomendated.append(_similarities_[i])
                    i += 1
        except Exception as e:
            e.__str__()
        return offers_recomendated


class UpdateSettingsForGraduate(UpdateView):
    template_name = 'setting_for_graduate_user.html'
    model = Settings
    form_class = SettingsForm
    success_url = reverse_lazy('list_job_offers_by_user_preferences_root')
    url = Url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = self.success_url
        self.url.url = self.request.META.get('HTTP_REFERER')
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'form': SettingsForm()
        }
        try:
            if request.method == 'POST':
                form = SettingsForm(data=request.POST)
                if form.is_valid():
                    self.object = self.get_object()
                    form = self.get_form()
                    form.save()
                    messages.success(request, "Ajustes guardados satisfactoriamente.")
                    super().post(request, *args, **kwargs)
                    return redirect(self.url.url)
                else:
                    data['form'] = form
        except Exception as e:
            e.__str__()
        return render(request, self.template_name, data)
