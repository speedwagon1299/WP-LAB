from django.shortcuts import render
from .forms import GrocForm

PRICES = {
    "Wheat": "₹40",
    "Jaggery": "₹60",
    "Dal": "₹80",
}

def index(request):
    selected_items = []
    if request.method == 'POST':
        form = GrocForm(request.POST)
        if form.is_valid():
            selected_items = form.cleaned_data['items']
    else:
        form = GrocForm()

    items_with_prices = [(item, PRICES[item]) for item in selected_items]

    return render(request, 'index.html', {'form': form, 'items_with_prices': items_with_prices})
