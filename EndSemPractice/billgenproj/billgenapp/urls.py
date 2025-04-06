from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('table_page', table_page, name='table_page')
]