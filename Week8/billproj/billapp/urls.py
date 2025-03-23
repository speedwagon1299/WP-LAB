from django.urls import path
from . import views

urlpatterns = [
    path('bill/', views.bill, name='bill'),
    path('bill_success/', views.bill_success, name='bill_success'),
]
