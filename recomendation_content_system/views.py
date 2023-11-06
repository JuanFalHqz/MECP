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
from recomendation_content_system.forms import ContentForm
from recomendation_content_system.models import Contenido
from recomendation_profile_system.models import Settings
from student.models import Ability, Student


# Clases de Contenidos
class DetailProfessionalContent(LoginRequiredMixin, TemplateView):
    template_name = 'detail_contenido_to_student.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['pk']:
            context['content'] = Contenido.objects.get(id=context['pk'])
            if is_student(request.user):
                self.template_name = 'detail_contenido_to_student.html'
                return self.render_to_response(context)
            #
            rppjo = ProfessionalContentRecommender(self.request.user.student)
            context['data'] = rppjo.get_recommendations_by_content(context['pk'])
            context['umbral'] = rppjo.setting.relevance_umbral
            context['count'] = len(context['data'])

        return self.render_to_response(context)


class ListContent(LoginRequiredMixin, ListView):
    template_name = 'list_contenidos.html'
    model = Contenido

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contenido'] = Contenido.objects.all()
        context['form'] = ContentForm()
        return context


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


class ProfessionalContentRecommender:
    """
    Obtener los contenidos rcomendados
    requiere:
        lista de contenidos
        contenido visto
    retorna
        Recomendacion de contenidos
    """
    all_content = ''
    setting = 0
    student = Student()
    list_content_to_recommender = 0

    def __init__(self, student):
        self.all_content = Contenido.objects.all()
        self.setting = Settings.objects.get(pk=student.user.settings.pk)
        student = student

    def get_recommendations_by_content(self, id):
        """
        Retorna una oferta de trabajo y los perfiles similares de acorde al umbral de similitud.
        """
        similarities = []

        oferta = ''
        try:
            r = Recommendation()
            # Obtiene las recomendaciones de contenido por el usuario en sesi'on
            for content in self.all_content:
                similarity = r.get_similarity(self.student.str_meta_data_for_content(), content.str_meta_data())
                similarities.append({
                    'content': content,
                    'similarity': round(similarity * 100, 2)
                })
            # ordenar y tomar según la cantidad
            similarities.sort(key=lambda x: x['similarity'], reverse=True)
            if len(similarities) > self.setting.cant_element_to_show:
                _similarities_ = similarities
                similarities = []
                i = 0
                while i < 5:
                    similarities.append(_similarities_[i])
                    i += 1
        except Exception as e:
            e.__str__()
        return similarities
