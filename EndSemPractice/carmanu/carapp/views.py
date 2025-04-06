from django.shortcuts import render, redirect
from .forms import CarForm

def index(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            request.session['form_data'] = form.cleaned_data
            return redirect('result') 
            # return render(request, 'secondPage.html', form.cleaned_data)
    else:
        form = CarForm()
    return render(request, 'firstPage.html', {'form': form})

def result(request):
    data = request.session.get('form_data', {})
    return render(request, 'secondPage.html', data)
    