from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MarkForm

def firstPage(request):
	if request.method == 'POST':
		form = MarkForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			tot_marks = form.cleaned_data['tot_marks']
			request.session['name'] = name
			cgpa = int(tot_marks)/50
			request.session['cgpa'] = cgpa
			return redirect(reverse('secondPage'))	
	else:
		form = MarkForm()
	return render(request, 'firstPage.html', {'form': form})

def secondPage(request):
	name = request.session.get('name', 'NA')
	cgpa = request.session.get('cgpa', '0.0')
	return render(request, 'secondPage.html', {'name': name, 'cgpa': cgpa})