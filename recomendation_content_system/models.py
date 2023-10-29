from django.db import models

from exam.models import Course
from student.models import Ability


# Create your models here.
class Contenido (models.Model):
    titulo = models.CharField(verbose_name="Título",max_length=50)
    content = models.FileField(verbose_name="Archivo", upload_to="media/%Y/%m/%d")
    abilities = models.ManyToManyField(Ability)
    curses = models.ManyToManyField(Course)
    descripcion = models.TextField(verbose_name="Descripción")

