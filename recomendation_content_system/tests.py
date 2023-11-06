from django.test import TestCase

from exam.models import Course
from recomendation_content_system.models import Contenido
from student.models import Ability

# Create your tests here.

'''
Notas ....
Pendiente:
1- Llenar la BD con los contenidos ...
2- Ejecutar los test ...
3- 
'''


class AddCurses(TestCase):
    Course.objects.all().delete()
    Course.objects.create(course_name="Desarrollo de aplicaciones web", question_number=5, total_marks=100, )
    Course.objects.create(course_name="Desarrollo web con Laravel", question_number=5, total_marks=100, )
    Course.objects.create(course_name="Diseño de aplicaciones web", question_number=5, total_marks=100, )
    Course.objects.create(course_name="Gestión de base de datos", question_number=5, total_marks=100, )
    Course.objects.create(course_name="Administración de redes informáticas", question_number=5, total_marks=100, )


class AddContenido(TestCase):
    a = Ability.objects.all()
    curse = Course.objects.all()
    Contenido.objects.all().delete()
    # 5 habilidades, puedes poner más
    c = Contenido.objects.create(titulo="Administración de Base de datos", content='profile_pic/Student/2.jpg',
                                 descripcion="")
    c.curses.add(curse.get(course_name='Gestión de base de datos'))
    c.abilities.add(a.get(ability='SQL'))
    c.abilities.add(a.get(ability='MySql'))
    c.abilities.add(a.get(ability='PostgreSQL'))
    c.abilities.add(a.get(ability='Diseño'))

    c = Contenido.objects.create(titulo="Mundo de datos", content='profile_pic/Student/2.jpg',
                                 descripcion="")
    c.curses.add(curse.get(course_name='Gestión de base de datos'))
    c.abilities.add(a.get(ability='SQL'))
    c.abilities.add(a.get(ability='Oracle'))
    c.abilities.add(a.get(ability='PostgreSQL'))
    c.abilities.add(a.get(ability='MongoDB'))
    c.abilities.add(a.get(ability='Diseño'))

    c = Contenido.objects.create(titulo="Diseñador Web", content='profile_pic/Student/2.jpg',
                                 descripcion="")
    c.curses.add(curse.get(course_name='Diseño de aplicaciones web'))
    c.curses.add(curse.get(course_name='Desarrollo de aplicaciones web'))
    c.abilities.add(a.get(ability='Diseño'))
    c.abilities.add(a.get(ability='HTML'))
    c.abilities.add(a.get(ability='CSS'))
    c.abilities.add(a.get(ability='Bootstrap'))

    c = Contenido.objects.create(titulo="Diseñador UI UX", content='profile_pic/Student/2.jpg',
                                 descripcion="")
    c.curses.add(curse.get(course_name='Diseño de aplicaciones web'))
    c.abilities.add(a.get(ability='Diseño'))
    c.abilities.add(a.get(ability='Diseño UI UX'))
    c.abilities.add(a.get(ability='HTML'))
    c.abilities.add(a.get(ability='CSS'))
    c.abilities.add(a.get(ability='Bootstrap'))

    c = Contenido.objects.create(titulo="Desarrollador frontend", content='profile_pic/Student/2.jpg',
                                 descripcion="")
    c.curses.add(curse.get(course_name='Diseño de aplicaciones web'))
    c.abilities.add(a.get(ability='Diseño UI UX'))
    c.abilities.add(a.get(ability='HTML'))
    c.abilities.add(a.get(ability='CSS'))
    c.abilities.add(a.get(ability='Bootstrap'))
    c.abilities.add(a.get(ability='Vue.js'))
