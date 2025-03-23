from django.shortcuts import render
from .models import Institute
from .forms import InstituteForm

def index(request):
    institutes = Institute.objects.all()
    return render(request, 'index.html', {"institutes": institutes})