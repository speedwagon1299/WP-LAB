from django.urls import path
from .views import *

urlpatterns = [
    path('vote_page', vote_page, name='vote_page'),
    path('results', results, name='results')
]