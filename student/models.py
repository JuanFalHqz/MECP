from django.db import models
from django.contrib.auth.models import User


class Ability(models.Model):
    ability = models.CharField(max_length=100, verbose_name='habilidad')

    def __str__(self):
        return self.ability


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Student/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    abilities = models.ManyToManyField(Ability)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name

    def str_meta_data(self):
        text = ''
        text += ' '
        text += self.address
        for ability in self.abilities.all():
            text += ' '
            text += ability.ability
        return text
