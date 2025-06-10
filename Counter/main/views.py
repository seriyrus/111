from django.shortcuts import render
from .forms import StudentForm, CourseForm
from .models import Student, Course

def index(request):
    courseform = CourseForm()
    studentform = StudentForm()
    
    if request.method == "POST" and 'first_name' in request.POST:
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            newstudent = studentform.save()
            newstudent.save()
        else:
            studentform = StudentForm()
    if request.method == "POST" and 'course' in request.POST:
        courseform =  CourseForm(request.POST)
        if courseform.is_valid():
            newscourse = courseform.save()
            newscourse.save()
        else:
             courseform = CourseForm()
    else:
        courseform = CourseForm()
        studentform = StudentForm()
    
    students = Student.objects.all()
    data = {
        'students':students,
        'studentform':studentform,
        'courseform':courseform,
    } 
    return render(request, 'main/index.html', data)
