from django.db import models

class Works(models.Model):
    person_name = models.CharField(max_length=128, unique=True)
    company_name = models.CharField(max_length=128)
    salary = models.FloatField(default=0.0)

class Lives(models.Model):
    person_name = models.CharField(max_length=128, unique=True)
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)