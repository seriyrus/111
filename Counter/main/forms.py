from django import forms
from .models import Course, Student

class CourseForm(forms.ModelForm):
    course = forms.CharField(max_length=50, label='Курс', widget=forms.TextInput(attrs={'class':'courseFormcourse'}))
    class Meta:
        model = Course
        fields = '__all__'
        
class StudentForm(forms.ModelForm):
    surname = forms.CharField(max_length=50, label='Фамилия', widget=forms.TextInput(attrs={'class':'studentFormsurname'}))
    first_name = forms.CharField(max_length=50, label='Имя', widget=forms.TextInput(attrs={'class':'studentFormfirstname'}))
    last_name = forms.CharField(max_length=50, label='Отчество', widget=forms.TextInput(attrs={'class':'studentFormlastname'}))
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type':'date', 'class':'studentFormdate'}))
    courses = forms.ModelChoiceField(queryset=Course.objects.all(),label='курс')
    class Meta:
        model = Student
        fields = '__all__'
