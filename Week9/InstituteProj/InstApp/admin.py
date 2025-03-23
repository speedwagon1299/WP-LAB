from django.contrib import admin
from .models import Institute

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('institute_id', 'name', 'num_courses') 