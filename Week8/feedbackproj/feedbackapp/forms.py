from django import forms

class FeedbackForm(forms.Form):
    COURSES = [
        ('ASP-XML', 'ASP-XML'),
        ('DotNET', 'DotNET'),
        ('JavaPro', 'JavaPro'),
        ('Unix', 'Unix'),
        ('C', 'C'),
        ('C++', 'C++'),
    ]

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Name")
    subject = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Subject")
    course = forms.ChoiceField(choices=COURSES, widget=forms.Select(attrs={"class": "form-control"}), label="Course")
    feedback = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label="Feedback")
