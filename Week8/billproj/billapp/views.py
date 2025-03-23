from django.shortcuts import render, redirect
from .forms import BillForm
from django.urls import reverse

def bill(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            request.session['brand'] = form.cleaned_data['brand']
            request.session['items'] = form.cleaned_data['items']
            request.session['quantity'] = form.cleaned_data['quantity']
            return redirect(reverse('bill_success'))
    else:
        form = BillForm()
    return render(request, 'bill.html', {'form': form})

def bill_success(request):
    brand = request.session.get('brand')
    items = request.session.get('items')
    quantity = int(request.session.get('quantity'))
    total = (len(items) * 5000 + 10000) * quantity  # Example cost calculation
    return render(request, 'bill_success.html', {'brand': brand, 'items': items, 'quantity': quantity, 'total': total})
