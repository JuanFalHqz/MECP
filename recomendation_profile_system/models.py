from django.db import models

from exam.models import Course
from student.models import Student


# Create your models here.
class Profile(models.Model):
    competencias = models.ManyToManyField(Course)
    estudiante = models.OneToOneField(Student, on_delete=models.DO_NOTHING)

