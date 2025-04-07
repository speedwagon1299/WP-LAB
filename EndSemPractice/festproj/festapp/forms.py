from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'rollno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Roll Number'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-select', 'placeholder': 'Gender'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email ID'}),
            'dept': forms.RadioSelect(attrs={'class': 'form-select', 'placeholder': 'Department'})
        }