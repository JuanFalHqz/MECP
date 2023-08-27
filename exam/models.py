from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    date = models.DateTimeField(auto_now=True)

class Question1(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    marks=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    question1=models.CharField(max_length=600)
    resp=models.CharField(max_length=200, blank=True)
    answer=models.CharField(max_length=200)

class Question2(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    marks=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    question2=models.CharField(max_length=600)
    Verdadero=models.BooleanField(True)
    Falso=models.BooleanField(False)
    cat=(('Verdadero','Verdadero'),('Falso','Falso'))
    answer=models.CharField(max_length=200,choices=cat)
