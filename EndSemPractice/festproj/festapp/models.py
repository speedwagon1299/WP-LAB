from django.db import models

GENDER_CHOICES = [(x,x) for x in ['Male', 'Female']]

DEPARTMENT_CHOICES = [(x,x) for x in ['CSE', 'ECE', 'EEE']]

class Student(models.Model):
    name = models.CharField(max_length=128)
    rollno = models.IntegerField(default=0)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=None)
    email = models.EmailField(max_length=128)
    dept = models.CharField(max_length=128, choices=DEPARTMENT_CHOICES, default=None)