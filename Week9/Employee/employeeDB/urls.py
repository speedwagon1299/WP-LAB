from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_works', views.add_works, name='add_works'),
    path('add_lives', views.add_lives, name='add_lives'),
    path('search_results/', views.search_results, name='search_results'),
]