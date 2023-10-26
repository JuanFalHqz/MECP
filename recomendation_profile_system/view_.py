from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from exam.views import is_student
from recomendation_profile_system.forms import ProfessionalOfferForm, SettingsForm
from recomendation_profile_system.models import ProfessionalOffer, Settings
from student.models import Ability, Student


#   JobOffer Classes
class AddProfessionalOffer(LoginRequiredMixin, CreateView):
    template_name = 'add_professional_offer.html'
    model = ProfessionalOffer
    form_class = ProfessionalOfferForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abilities'] = Ability.objects.all()
        context['root'] = reverse_lazy('add_job_offer_post_root')
        context['modalities'] = ['Teletrabajo', 'Presencial', 'Híbrido']
        return context


class UpdateProfessionalOffer(LoginRequiredMixin, UpdateView):
    template_name = 'update_professional_offer.html'
    model = ProfessionalOffer
    form_class = ProfessionalOfferForm

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            pk = context['object'].pk
            context['job_offer'] = ProfessionalOffer.objects.get(pk=pk)
            context['abilities_select'] = ProfessionalOffer.objects.get(pk=pk).abilities.all()
            context['abilities'] = Ability.objects.all()
            context['root'] = reverse_lazy('update_job_offer_post_root')
            context['modalities'] = ['Teletrabajo', 'Presencial', 'Híbrido']
            return context
        except Exception as e:
            e.__str__


class DetailProfessionalOffer(LoginRequiredMixin, TemplateView):
    template_name = 'detail_professional_offer.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['pk']:
            context['job_offer'] = ProfessionalOffer.objects.get(id=context['pk'])
            if is_student(request.user):
                self.template_name = 'detail_professional_offer_to_studet.html'
                return self.render_to_response(context)
            x = ProfessionalOffer.objects.get(id=context['pk'])
            y = x.abilities.all()
            #
            rppjo = ProfessionalProfileRecommender(self.request.user.teacher)
            context['data'] = rppjo.get_recommendations_by_offer(context['pk'])
            context['umbral'] = rppjo.setting.relevance_umbral
            context['count'] = len(context['data'])

        return self.render_to_response(context)


class DeleteProfessionalOffer(LoginRequiredMixin, DeleteView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un proyecto'
        context['singular'] = 'Oferta profesional'
        context['plural'] = 'Ofertas profesionales'
        context['url_success'] = reverse_lazy('project_list_root')
        context['action'] = 'delete'
        return context

    def get(self, request):
        deleted = False
        errors = ''

        pk = request.GET.get('pk')
        list_to_deleted = request.GET.getlist('list_id[]')
        # Si hay lista con elementos a eliminar, se eliminan
        if (list_to_deleted):
            try:
                for item in list_to_deleted:
                    ProfessionalOffer.objects.get(pk=item).delete()
                deleted = True
            except Exception as e:
                errors += str(e.__str__())
            data = {
                'deleted': deleted,
                'errors': errors,
            }
            return JsonResponse(data)
        try:
            ProfessionalOffer.objects.get(pk=pk).delete()
            deleted = True
        except Exception as e:
            errors += str(e.__str__())
        data = {
            'deleted': deleted,
            'errors': errors,
        }
        # d = json.dumps(data)
        return JsonResponse(data)


class ListProfessionalOffers(LoginRequiredMixin, ListView):
    template_name = 'list_professional_offer.html'
    model = ProfessionalOffer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_offer'] = ProfessionalOffer.objects.filter(teacher=self.request.user.teacher).order_by('-date')
        return context


class ProfessionalProfileRecommender:
    """
    Obtener los perfiles rcomendados
    requiere:
        lista de perfiles
        oferta laboral
    retorna
        lista de perfiles
    """
    professional_offer = ''
    professional_profiles = ''
    teacher = ''
    setting = ''

    def __init__(self, teacher):
        self.professional_offer = ProfessionalOffer.objects.filter(teacher=teacher)
        self.professional_profiles = Student.objects.all()
        self.teacher = teacher
        self.professional_profiles = Student.objects.all()
        self.setting = Settings.objects.get(user_id=teacher.user.settings.pk)

    def get_professional_offer_text(self):
        list = []
        try:
            for job in self.professional_offer:
                list.append({
                    'id': job.pk,
                    'meta': job.str_meta_data()
                })
            return list
        except Exception as e:
            e.__str__()

    def get_profiles_text(self):
        list = []
        try:
            for student in self.professional_profiles:
                list.append({
                    'id': student.pk,
                    'meta': student.str_meta_data()
                })
            return list
        except Exception as e:
            e.__str__()

    def get_recommendations_by_offer(self, id):
        """
        Retorna una oferta de trabajo y los perfiles similares de acorde al umbral de similitud.
        """
        ofertas = self.get_professional_offer_text()
        oferta = ''
        try:
            for o in ofertas:
                if o['id'] == id:
                    oferta = o

            perfiles = self.get_profiles_text()
            r = Recommendation()

            similarities = []
            for profile in perfiles:
                similarity = r.get_similarity(oferta['meta'], profile['meta'])
                if similarity * 100 >= self.setting.relevance_umbral:
                    similarities.append({
                        'profile': Student.objects.get(pk=profile['id']),
                        'similarity': round(similarity * 100, 2)
                    })
            # ordenar y tomar según la cantidad
            similarities.sort(key=lambda x: x['similarity'], reverse=True)
            if len(similarities) > self.setting.cant_element_to_show:
                _similarities_ = similarities
                similarities = []
                i = 0
                while i < self.setting.cant_element_to_show:
                    similarities.append(_similarities_[i])
                    i += 1
        except Exception as e:
            e.__str__()
        return similarities


class Recommendation:
    @staticmethod
    def get_similarity(text1, text2):
        # Crear un vectorizador TF-IDF
        vectorizador = TfidfVectorizer()

        # Vectorizar los textos
        vector_texto1 = vectorizador.fit_transform([text1])
        vector_texto2 = vectorizador.transform([text2])

        # Calcular la similitud de coseno entre los vectores
        return cosine_similarity(vector_texto1, vector_texto2)[0][0]


#   Setting Classes
class UpdateSettings(LoginRequiredMixin, UpdateView):
    template_name = 'settings.html'
    model = Settings
    form_class = SettingsForm
    success_url = reverse_lazy('list_job_offers_root')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = self.success_url
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
                    response = super().post(request, *args, **kwargs)
                    return response
                else:
                    data['form'] = form
        except Exception as e:
            e.__str__()
        return render(request, self.template_name, data)


def add_professional_offer(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        modality = request.POST.get('modality')
        address = request.POST.get('address')
        description = request.POST.get('description')
        abilities = request.POST.getlist('abilities[]')
        teacher = request.user.teacher
        # Validations
        if title == '' or title is None:
            return JsonResponse('Escriba el título', 300)
        if modality == '' or modality is None:
            return JsonResponse('Seleccione la modalidad', 300)
        if (address == '' and not modality == "Teletrabajo") or (address is None and not modality == "Teletrabajo"):
            return JsonResponse('Escriba la dirección', 300)
        if len(abilities) == 0 or abilities is None:
            return JsonResponse('Seleccione al menos una habilidad', 300)
        # Save
        try:
            job_offer = ProfessionalOffer.objects.create(title=title, address=address, teacher=teacher, modality=modality,
                                                         description=description, date=datetime.now().date())
            for ability_pk in abilities:
                job_offer.abilities.add(ability_pk)
            return JsonResponse({'pk': job_offer.pk}, status=201)
        except Exception as e:
            e.__str__()


def update_professional_offer(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        modality = request.POST.get('modality')
        pk = int(request.POST.get('pk'))
        address = request.POST.get('address')
        description = request.POST.get('description')
        abilities = request.POST.getlist('abilities[]')
        # Validations
        if title == '' or title is None:
            return JsonResponse('Escriba el título', 300)
        if modality == '' or modality is None:
            return JsonResponse('Seleccione la modalidad', 300)
        if (address == '' and not modality == "Teletrabajo") or (address is None and not modality == "Teletrabajo"):
            return JsonResponse('Escriba la dirección', 300)
        if len(abilities) == 0 or abilities is None:
            return JsonResponse('Seleccione al menos una habilidad', 300)
        # Save
        try:
            job_offer = ProfessionalOffer.objects.get(pk=pk)

            job_offer.title = title
            job_offer.modality = modality
            job_offer.address = address
            job_offer.description = description
            job_offer.abilities.clear()
            for ability_pk in abilities:
                job_offer.abilities.add(ability_pk)
            job_offer.save()
            return JsonResponse({'pk': job_offer.pk}, status=201)
        except Exception as e:
            e.__str__()
