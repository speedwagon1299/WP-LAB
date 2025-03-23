from django import forms

CHOICES = [
	('good', 'Good'),
	('satis', 'Satisfactory'),
	('bad', 'Bad')
]

class ReviewForm(forms.Form):
	review = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={"class": "form-check-input"}), label="How is the book ASP.NET with C# by Vipul Prakashan")