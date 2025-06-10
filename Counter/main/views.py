from django.shortcuts import render
from .forms import Form1
from .models import Student, Course

def index(request):
    students = Student.objects.all()
    data = {
        'students':students,
    }
    return render(request, 'main/index.html', data)
