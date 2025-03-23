from django import forms

BRANDS = [('HP', 'HP'), ('Nokia', 'Nokia'), ('Samsung', 'Samsung'), ('Motorola', 'Motorola'), ('Apple', 'Apple')]
ITEMS = [('Mobile', 'Mobile'), ('Laptop', 'Laptop')]

class BillForm(forms.Form):
    brand = forms.ChoiceField(widget=forms.RadioSelect, choices=BRANDS, label="Select Brand")
    items = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=ITEMS, label="Select Items")
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}), label="Quantity")
