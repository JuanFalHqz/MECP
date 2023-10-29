# Create your views here.
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
from recomendation_content_system.forms import ContenidoForm
from recomendation_content_system.models import Contenido
from student.models import Ability, Student

# Clases de Contenidos

class list_contenidos(LoginRequiredMixin, ListView):
    template_name = 'list_contenidos.html'
    model = Contenido

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contenido'] = Contenido.objects.all()
        return context

