from django.urls import path
from .views import index, cadClientes

urlpatterns = [
    path('', index, name="index"),
    path('/cadClientes', cadClientes, name="cadClientes"),
]
