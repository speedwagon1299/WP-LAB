from django.contrib import admin
from .models import *

admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)