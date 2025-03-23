from django.shortcuts import render, redirect
from .forms import RegForm
from django.urls import reverse

def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            
            request.session['username'] = username
            request.session['email'] = email
            request.session['phone'] = phone
            
            return redirect(reverse('success'))  
    else:
        form = RegForm()

    return render(request, 'register.html', {'form': form})


def success(request):
    username = request.session.get('username', 'Guest')
    email = request.session.get('email', 'NA')
    phone = request.session.get('phone', 'NA')

    return render(request, 'success.html', {'username': username, 'email': email, 'phone': phone})