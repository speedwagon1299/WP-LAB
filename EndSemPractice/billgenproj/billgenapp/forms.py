from django import forms

ITEM_CHOICES = ['Wheat', 'Jaggery', 'Dal']

class Table(forms.Form):
    items = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-select'}), label="Items",
                                      choices=[(x,x) for x in ITEM_CHOICES])