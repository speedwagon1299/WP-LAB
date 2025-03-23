from django.contrib import admin
from django.urls import path, include
import employeeDB

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employeeDB.urls'))
]
