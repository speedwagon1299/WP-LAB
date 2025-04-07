from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_branch', add_branch, name='add_branch'),
    path('add_course', add_course, name='add_course'),
    path('add_teacher', add_teacher, name='add_teacher'),
    path('add_student', add_student, name='add_student'),
    path('update_branch/<int:pk>/', update_branch, name='update_branch'),
    path('update_course/<int:pk>/', update_course, name='update_course'),
    path('update_teacher/<int:pk>/', update_teacher, name='update_teacher'),
    path('update_student/<int:pk>/', update_student, name='update_student'),
    path('delete_branch/<int:pk>/', delete_branch, name='delete_branch'),
    path('delete_course/<int:pk>/', delete_course, name='delete_course'),
    path('delete_teacher/<int:pk>/', delete_teacher, name='delete_teacher'),
    path('delete_student/<int:pk>/', delete_student, name='delete_student'),
]