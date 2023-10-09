from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from recomendation_profile_system.forms import JobOfferForm, SettingsForm
from recomendation_profile_system.models import JobOffer, Settings
from student.models import Ability, Student


#   JobOffer Classes
class AddJobOffer(CreateView):
    template_name = 'professional_profile_add.html'
    model = JobOffer
    form_class = JobOfferForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abilities'] = Ability.objects.all()
        context['root'] = reverse_lazy('add_job_offer_post_root')
        return context


class UpdateJobOffer(UpdateView):
    template_name = 'update_job_offer.html'
    model = JobOffer
    form_class = JobOfferForm

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            pk = context['object'].pk
            context['job_offer'] = JobOffer.objects.get(pk=pk)
            context['abilities_select'] = JobOffer.objects.get(pk=pk).abilities.all()
            context['abilities'] = Ability.objects.all()
            context['root'] = reverse_lazy('update_job_offer_post_root')
            return context
        except Exception as e:
            e.__str__


class DetailJobOffer(TemplateView):
    template_name = 'detail_job_offer.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['pk']:
            x = JobOffer.objects.get(id=context['pk'])
            y = x.abilities.all()
            context['job_offer'] = JobOffer.objects.get(id=context['pk'])
            #
            rppjo = RecommendationProfessionalProfile(self.request.user.teacher)
            context['data'] = rppjo.get_recommended_by_offer(context['pk'])
            context['umbral'] = Settings.objects.get(id=1).relevance_umbral

        return self.render_to_response(context)


class DeleteJobOffer(DeleteView):
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
                    JobOffer.objects.get(pk=item).delete()
                deleted = True
            except Exception as e:
                errors += str(e.__str__())
            data = {
                'deleted': deleted,
                'errors': errors,
            }
            return JsonResponse(data)
        try:
            JobOffer.objects.get(pk=pk).delete()
            deleted = True
        except Exception as e:
            errors += str(e.__str__())
        data = {
            'deleted': deleted,
            'errors': errors,
        }
        # d = json.dumps(data)
        return JsonResponse(data)


class ListJobOffer(ListView):
    template_name = 'list_job_offer.html'
    model = JobOffer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_offer'] = JobOffer.objects.filter(teacher=self.request.user.teacher)
        return context


class ListStudent(ListView):
    template_name = 'list_professional_profile.html'
    model = Student

    def get_context_data(self, *, object_list=None, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['profiles_by'] = JobOffer.objects.filter(teacher=self.request.user.teacher)
            rppjo = RecommendationProfessionalProfile(self.request.user.teacher)
            context['data'] = rppjo.get_profiles_recommended()
            context['umbral'] = Settings.objects.get(id=1).relevance_umbral
            return context
        except Exception as e:
            e.__str__()


class RecommendationProfessionalProfile:
    """
    Obtener los perfiles rcomendados
    requiere:
        lista de perfiles
        oferta laboral
    retorna
        lista de perfiles
    """
    job_offer = ''
    professional_profiles = ''
    teacher = ''
    setting = ''

    def __init__(self, teacher):
        self.job_offer = JobOffer.objects.filter(teacher=teacher)
        self.professional_profiles = Student.objects.all()
        self.teacher = teacher
        self.professional_profiles = Student.objects.all()
        self.setting = RecommendationSystemSettings().get_all_setting()

    def get_job_offer_to_text(self):
        list = []
        try:
            for job in self.job_offer:
                list.append({
                    'id': job.pk,
                    'meta': job.str_meta_data()
                })
            return list
        except Exception as e:
            e.__str__()

    def get_profiles_to_text(self):
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

    def get_profiles_recommended(self):
        """
        Retorna una lista con las oferta de trabajo y los perfiles similares de acorde al umbral de similitud.
        """
        profiles_similarities = []
        ofertas = self.get_job_offer_to_text()
        perfiles = self.get_profiles_to_text()
        r = Recommendation()
        for offer in ofertas:
            similarities = []
            for profile in perfiles:
                similarity = r.similarity(offer['meta'], profile['meta'])
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
            profiles_similarities.append({
                'offer': JobOffer.objects.get(id=offer['id']),
                'profiles': similarities
            })
            profiles_similarities
        return profiles_similarities

    def get_recommended_by_offer(self, id):
        """
        Retorna una oferta de trabajo y los perfiles similares de acorde al umbral de similitud.
        """
        ofertas = self.get_job_offer_to_text()
        oferta = ''
        for o in ofertas:
            if o['id'] == id:
                oferta = o

        perfiles = self.get_profiles_to_text()
        r = Recommendation()

        similarities = []
        for profile in perfiles:
            similarity = r.similarity(oferta['meta'], profile['meta'])
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

        return similarities
    998

class Recommendation():
    def similarity(self, text1, text2):
        # Crear un vectorizador TF-IDF
        vectorizador = TfidfVectorizer()

        # Vectorizar los textos
        vector_texto1 = vectorizador.fit_transform([text1])
        vector_texto2 = vectorizador.transform([text2])

        # Calcular la similitud de coseno entre los vectores
        return cosine_similarity(vector_texto1, vector_texto2)[0][0]


#   Setting Classes
class RecommendationSystemSettings:
    setting = ''

    def __init__(self):
        self.setting = Settings.objects.get(id=1)

    def get_all_setting(self):
        return self.setting

    def get_cant_element_to_show(self):
        return self.setting.cant_element_to_show

    def get_relevance_umbral(self):
        return self.setting.relevance_umbral

    def set_cant_element_to_show(self, cant_element_to_show):
        self.setting.cant_element_to_show = cant_element_to_show
        self.setting.save()

    def set_relevance_umbral(self, relevance_umbral):
        self.setting.relevance_umbral = relevance_umbral
        self.setting.save()


class UpdateSettings(UpdateView):
    template_name = 'settings.html'
    model = Settings
    form_class = SettingsForm
    success_url = reverse_lazy('list_profiles_root')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = self.success_url
        return context


def add_job_offer(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        address = request.POST.get('address')
        abilities = request.POST.getlist('abilities[]')
        teacher = request.user.teacher
        # Validations
        if title == '' or title is None:
            return JsonResponse('Escriba el título', 300)
        if address == '' or address is None:
            return JsonResponse('Escriba la dirección', 300)
        if len(abilities) == 0 or abilities is None:
            return JsonResponse('Seleccione al menos una habilidad', 300)
        # Save
        try:
            job_offer = JobOffer.objects.create(title=title, address=address, teacher=teacher)
            for ability_pk in abilities:
                job_offer.abilities.add(ability_pk)
            return JsonResponse({'pk': job_offer.pk}, status=201)
        except Exception as e:
            e.__str__()


def update_job_offer(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        pk = int(request.POST.get('pk'))
        address = request.POST.get('address')
        abilities = request.POST.getlist('abilities[]')
        # Validations
        if title == '' or title is None:
            return JsonResponse('Escriba el título', 300)
        if address == '' or address is None:
            return JsonResponse('Escriba la dirección', 300)
        if len(abilities) == 0 or abilities is None:
            return JsonResponse('Seleccione al menos una habilidad', 300)
        # Save
        try:
            job_offer = JobOffer.objects.get(pk=pk)

            job_offer.title = title
            job_offer.address = address
            job_offer.abilities.clear()
            for ability_pk in abilities:
                job_offer.abilities.add(ability_pk)
            job_offer.save()
            return JsonResponse({'pk': job_offer.pk}, status=201)
        except Exception as e:
            e.__str__()
