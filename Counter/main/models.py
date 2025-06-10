from django.db import models


class Course(models.Model):
    course = models.CharField(max_length=50)
    
    def __str__(self):
        return self.course

class Student(models.Model):
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'{self.surname} {self.first_name} {self.last_name}: {self.course}'