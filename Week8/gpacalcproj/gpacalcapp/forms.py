from django import forms

class MarkForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Name")
	tot_marks = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}), label="Total Marks")