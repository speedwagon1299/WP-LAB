from django.shortcuts import render, redirect
from .models import Category, Page
from .forms import CategoryForm, PageForm

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()

    categories = Category.objects.all()
    return render(request, 'directory/add_category.html', {'form': form, 'categories': categories})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PageForm()

    pages = Page.objects.all()
    return render(request, 'directory/add_page.html', {'form': form, 'pages': pages})

def index(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'directory/index.html', {'categories': categories, 'pages': pages})
