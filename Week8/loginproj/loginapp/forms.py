from django import forms

class RegForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Username")
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), required=False, label="Password")
	email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control"}), required=False, label="Email")
	phone = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}), required=False, label="Phone Number")