from django import forms

CAR_CHOICES = [
    ('Maruti', 'Suzuki'), ('Toyota', 'Innova'), ('Honda', 'Civic')
]

GENDER_CHOICES = [
    ('M', 'Male'), ('F', 'Female')
]

SEMESTER_CHOICES = [
    ('I', 'First'), ('II', 'Second'), ('III', 'Third'), ('IV', 'Fourth')
]

COURSE_CHOICES = [
    ('Math101', 'Math1'), ('English101','English1'), ('Math102', 'Math2')
]

HOBBY_CHOICES = [
    'Sports', 'Music', 'Art'
]

class CarForm(forms.Form):

    # Radio Button Group
    # ChoiceField - RadioSelect
    car = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-select'}), choices=CAR_CHOICES, label="Car")
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-select'}), choices=GENDER_CHOICES, label="Gender")

    # Drop Down Select
    # ChoiceField - Select
    semester = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}), choices=SEMESTER_CHOICES, label="Semester")

    # Single Checkbox
    # BooleanField - CheckboxInput
    scholarship = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-select'}), label="Apply for Scholarship")
    
    # Drop Down Radio (Multiple Select)
    # MultipleChoiceField - CheckboxSelectMultiple
    courses = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-select'}), choices=COURSE_CHOICES, label="Courses")

    


