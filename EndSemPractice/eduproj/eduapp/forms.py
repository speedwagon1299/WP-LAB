from django import forms
from .models import *

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}, placeholder='Branch Name'),
            'code': forms.NumberInput(attrs={'class': 'form-control'}, placeholder='Branch Code')
        }    

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}, placeholder='Course Name'),
            'code': forms.NumberInput(attrs={'class': 'form-control'}, placeholder='Course Code'),
            'credits': forms.NumberInput(attrs={'class': 'form-control'}, placeholder='Credits'),
            'branch': forms.RadioSelect(attrs={'class': 'form-select'}, placeholder='Branch')
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}, placeholder='Teacher Name'),
            'branch': forms.RadioSelect(attrs={'class': 'form-select'}, placeholder='Branch'),
            'section': forms.TextInput(attrs={'class': 'form-control'}, placeholder='Section'),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}, placeholder='Qualification'),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'year', 'branch', 'section', 'rollno', 'courses']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}, placeholder='Student Name'),
            'year': forms.RadioSelect(attrs={'class': 'form-select'}, placeholder='Year'),
            'branch': forms.RadioSelect(attrs={'class': 'form-select'}, placeholder='Branch'),
            'section': forms.TextInput(attrs={'class': 'form-control'}, placeholder='Section'),
            'rollno': forms.NumberInput(attrs={'class': 'form-control'}, placeholder='Roll Number'),
            'courses': forms.CheckboxSelectMultiple(attrs={'class': 'form-select'}, placeholder='Courses'),
        }