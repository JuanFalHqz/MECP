from django.db import models

from exam.models import Course
from student.models import Student, Ability
from teacher.models import Teacher


# Create your models here.
class JobOffer(models.Model):
    title = models.CharField(max_length=250, verbose_name="Título")
    address = models.CharField(max_length=250, verbose_name="dirección", null=True, blank=True)
    abilities = models.ManyToManyField(Ability)
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)

    def str_meta_data(self):
        text = ''
        text += ' '
        text += self.address
        for ability in self.abilities.all():
            text += ' '
            text += ability.ability
        return text


class Settings(models.Model):
    cant_element_to_show = models.PositiveIntegerField(verbose_name='Cantidad de elementos a mostrar', default=10)
    relevance_umbral = models.PositiveIntegerField(verbose_name='Umbral de relevancia', default=90)
