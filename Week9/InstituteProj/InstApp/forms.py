from django import forms
from .models import Institute

class InstituteForm(forms.Form):
    class Meta:
        model = Institute
        fields = ['institute_id', 'name', 'num_courses']
