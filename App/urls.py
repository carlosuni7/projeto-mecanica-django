from django.urls import path
from .views import ExcluirRegistro,Erro, index,Dash, Clientes, cadClientes, altCliente,exCliente,Mecanicos,exMecanico, Veiculos, altVeiculo,cadVeiculo,exVeiculo,Pecas, Orcamentos,exOrcamento, cadPeca, altPeca, exPeca

urlpatterns = [
    path('', index, name="index"),
    path('dashboard',Dash,name="dashboard"),
    path('excluir-registro/<str:tabela>/<int:pk>',ExcluirRegistro,name="excluir-registro"),
    path('error', Erro, name="error"),
    #  URL de clientes
    path('clientes',Clientes,name="clientes"),
    path('cadClientes', cadClientes, name="cadClientes"),
    path('altCliente/<int:pk>', altCliente, name="altCliente"),
    path('excluir-cliente/<int:pk>', exCliente, name="excluir-cliente"),
    # URL de mecanicos
    path('mecanicos',Mecanicos,name="mecanicos"),
    path('cadMecanico', cadClientes, name="cadMecanico"),
    path('excluir-mecanico/<int:pk>', exMecanico, name='excluir-mecanico'),
    # URL de veiculos
    path('veiculos',Veiculos,name="veiculos"),
    path('cadVeiculos', cadVeiculo, name="cadVeiculos"),
    path('altVeiculo/<int:pk>', altVeiculo, name="altVeiculo"),
    path('excluir-veiculo/<int:pk>', exVeiculo, name="excluir-veiculo"),
    # URL de peças
    path('pecas',Pecas,name="pecas"),
    path('cadPeca', cadPeca, name="cadPeca"),
    path('altPeca/<int:pk>', altPeca, name="altPeca"),
    path('excluir-peca/<int:pk>', exPeca, name="excluir-peca"),
    # URL de orçamentos
    path('orcamentos',Orcamentos,name="orcamentos"),
    path('excluir-orcamento/<int:pk>', exOrcamento, name="excluir-orcamento"),
]
