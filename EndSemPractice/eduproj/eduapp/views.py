from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    branches = Branch.objects.all()
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    context = {
        'branches': branches,
        'courses': courses,
        'teachers': teachers,
        'students': students 
    }
    return render(request, 'index.html', context=context)

def add_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BranchForm()
    return render(request, 'add_branch.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})
        

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})
                

def update_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BranchForm()
    return render(request, 'update_branch.html', {'form': form})

def update_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'update_course.html', {'form': form})
        

def update_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeacherForm()
    return render(request, 'update_teacher.html', {'form': form})


def update_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'update_student.html', {'form': form})

def delete_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BranchForm()
    return render(request, 'delete_branch.html', {'form': form})

def delete_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'delete_course.html', {'form': form})
        

def delete_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeacherForm()
    return render(request, 'delete_teacher.html', {'form': form})


def delete_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'delete_student.html', {'form': form})