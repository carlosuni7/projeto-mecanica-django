from django.urls import path
from .views import index, Clientes, cadClientes,Mecanicos, Veiculos, Pecas, Orcamentos

urlpatterns = [
    path('', index, name="index"),
    path('clientes',Clientes,name="clientes"),
    path('cadClientes', cadClientes, name="cadClientes"),
    path('mecanicos',Mecanicos,name="mecanicos"),
    # path('/cadMecanico', cadClientes, name="cadClientes"),
    path('veiculos',Veiculos,name="veiculos"),
    # path('/cadClientes', cadClientes, name="cadClientes"),
    path('pecas',Pecas,name="pecas"),
    # path('/cadClientes', cadClientes, name="cadClientes"),
    path('orcamentos',Orcamentos,name="orcamentos"),
]
