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
                

def update_branch(request, pk):
    branch = Branch.objects.get(pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST,instance=branch)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BranchForm()
    return render(request, 'update_branch.html', {'form': form, 'branch': branch})

def update_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'update_course.html', {'form': form, 'course': course})
        

def update_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeacherForm()
    return render(request, 'update_teacher.html', {'form': form, 'teacher': teacher})


def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'update_student.html', {'form': form, 'student': student})

def delete_branch(request, pk):
    branch = Branch.objects.get(pk=pk)
    branch.delete()
    return redirect('index')

def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('index')

def delete_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    teacher.delete()
    return redirect('index')

def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('index')