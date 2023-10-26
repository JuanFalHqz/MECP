from django.contrib.auth.models import User
from django.db import models

from exam.models import Course
from student.models import Student, Ability
from teacher.models import Teacher


# Create your models here.
class ProfessionalOffer(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    address = models.CharField(max_length=50, verbose_name="Dirección", null=True, blank=True)
    description = models.TextField(max_length=250, verbose_name='Descripción', null=True, blank=True)
    modality = models.CharField(max_length=15,
                                choices=[("Teletrabajo", "Teletrabajo"), ("Presencial", "Presencial"),
                                         ("Híbrido", "Híbrido")],
                                verbose_name='Modalidad')
    date = models.DateField(verbose_name="Fecha", auto_now=False, auto_created=True)
    abilities = models.ManyToManyField(Ability)
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title

    def str_meta_data(self):
        text = ''
        text += ' '
        if self.address is not None and self.address != '':
            text += self.address
        text += self.modality
        if self.description is not None and self.description != '':
            text += self.description
        for ability in self.abilities.all():
            text += ' '
            text += ability.ability
        return text


class Settings(models.Model):
    cant_element_to_show = models.PositiveIntegerField(verbose_name='Cantidad de elementos a mostrar', default=10)
    relevance_umbral = models.PositiveIntegerField(verbose_name='Umbral de relevancia', default=90)
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
