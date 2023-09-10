from django.contrib import admin
from .models import Question, Question1, Question2, Course, Student, Result

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Result)
admin.site.register(Question)
admin.site.register(Question1)
admin.site.register(Question2)
