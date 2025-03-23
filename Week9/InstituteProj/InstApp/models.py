from django.db import models

class Institute(models.Model):
    institute_id = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    num_courses = models.IntegerField(default=0)