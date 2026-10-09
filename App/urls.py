from django.urls import path
from .views import index,Dash, Clientes, cadClientes, altCliente,exCliente,Mecanicos, Veiculos, altVeiculo,cadVeiculo,exVeiculo,Pecas, Orcamentos, cadPeca, altPeca, exPeca

urlpatterns = [
    path('', index, name="index"),
    path('dashboard',Dash,name="dashboard"),
    #  URL de clientes
    path('clientes',Clientes,name="clientes"),
    path('cadClientes', cadClientes, name="cadClientes"),
    path('altCliente/<int:pk>', altCliente, name="altCliente"),
    path('exCliente/<int:pk>', exCliente, name="exCliente"),
    # URL de mecanicos
    path('mecanicos',Mecanicos,name="mecanicos"),
    # path('/cadMecanico', cadClientes, name="cadClientes"),
    # URL de veiculos
    path('veiculos',Veiculos,name="veiculos"),
    path('cadVeiculos', cadVeiculo, name="cadVeiculos"),
    path('altVeiculo/<int:pk>', altVeiculo, name="altVeiculo"),
    path('axVeiculo/<int:pk>', exVeiculo, name="exVeiculo"),
    # URL de peças
    path('pecas',Pecas,name="pecas"),
    path('cadPeca', cadPeca, name="cadPeca"),
    path('altPeca/<int:pk>', altPeca, name="altPeca"),
    path('exPeca/<int:pk>', exPeca, name="exPeca"),
    # URL de orçamentos
    path('orcamentos',Orcamentos,name="orcamentos"),
]
