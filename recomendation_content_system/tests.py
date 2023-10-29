from django.test import TestCase

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
class AddContenido(TestCase):
     contenido = [];
     c= Contenido(titulo="Programación Orientada a Objetos", content='media/nombre/',)
     c.abilities.add(c.get(Ability='Java'))
     c.curses.add(c.get(curses= 'Ejemplo'))

     c = Contenido(titulo="Ingenieria de Software", content='media/ISW/', )
     c.abilities.add(c.get(Ability='ISW'))
     c.curses.add(c.get(curses='Ejemplo'))

     c = Contenido(titulo="Base de Datos", content='media/BD/', )
     c.abilities.add(c.get(Ability='BD'))
     c.curses.add(c.get(curses='BD'))


     contenido.append()













     contenido.objects.all().delete()

     for i in contenido:
          a = contenido(contenido =i)
          a.save()
