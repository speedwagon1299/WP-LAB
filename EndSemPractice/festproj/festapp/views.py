from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm

def input_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_page')
    else:
        form = StudentForm()
    return render(request, 'input_page.html', {'form': form})

def view_page(request):
    students = Student.objects.all()
    return render(request, 'view_page.html', {'students': students})