from django.db import models

SECTION_CHOICES = [(x,x) for x in ['A','B', 'C']]
YEAR_CHOICES = [(x,x) for x in ['I', 'II', 'III', 'IV']]

class Branch(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)

    @property
    def credits(self):
        # Reverse relation for ManyToMany and ForeignKey, '_set' suffix
        return sum(course.credits for course in self.course_set.all())
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    credits = models.IntegerField(default=0)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=128)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    qualification = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=128)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    rollno = models.IntegerField(default=0)
    courses = models.ManyToManyField(Course)

    # Computed by backend so make it a property
    @property
    def credits(self):
        return sum(course.credits for course in self.courses.all())
    
    def __str__(self):
        return self.name
