from django.shortcuts import render, redirect
from .models import Works, Lives
from .forms import WorksForm, LivesForm

def index(request):
    works = Works.objects.all()
    lives = Lives.objects.all()
    works_form = WorksForm()
    lives_form = LivesForm()
    return render(request, 'index.html', {
        'works': works, 
        'lives': lives, 
        'works_form': works_form,
        'lives_form': lives_form
    })

def add_works(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WorksForm()
    return render(request, 'add_works.html', {'form': form})

def add_lives(request):
    if request.method == 'POST':
        form = LivesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LivesForm()
    return render(request, 'add_lives.html', {'form': form})

def search_results(request):
    company_name = request.GET.get('company_name')
    if company_name:
        results = Works.objects.filter(company_name=company_name).select_related()
        lives = Lives.objects.all()
        data = [
            {'person_name': result.person_name, 'city': lives.get(person_name=result.person_name).city}
            for result in results if lives.filter(person_name=result.person_name).exists()
        ]
        return render(request, 'search_results.html', {'company_name': company_name, 'results': data})
    return redirect('index')
