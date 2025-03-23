from django import forms

GROCERY_ITEMS = [
    ("Wheat", "Wheat - ₹40"),
    ("Jaggery", "Jaggery - ₹60"),
    ("Dal", "Dal - ₹80"),
]

class GrocForm(forms.Form):
    items = forms.MultipleChoiceField(
        choices=GROCERY_ITEMS,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-label"}),
        label="Select Items:"
    )
