from django.shortcuts import render
from .forms import *

def index(request):
    return render(request, 'index.html')

def table_page(request):
    if request.method == 'POST':
        form = Table(request.POST)
        if form.is_valid():
            conv = {'Wheat': '10','Jaggery': '20', 'Dal': '30'}
            item_price = [(x, conv.get(x,0)) for x in form.cleaned_data.get('items', {})]
            return render(request, 'table_page.html', {'form': form, 'item_price': item_price})
    else:
        form = Table()
    return render(request, 'table_page.html', {'form': form, 'item_price': []})