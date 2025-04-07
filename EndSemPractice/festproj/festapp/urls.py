from django.urls import path
from .views import *

urlpatterns = [
    path('input_page', input_page, name='input_page'),
    path('view_page', view_page, name='view_page')
]