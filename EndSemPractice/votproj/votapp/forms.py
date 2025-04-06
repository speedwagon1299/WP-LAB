from django import forms

VOTE_CHOICES = [(x, x) for x in ['A', 'B', 'C']]

class VoteForm(forms.Form):
    vote = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-select'}), choices=VOTE_CHOICES)