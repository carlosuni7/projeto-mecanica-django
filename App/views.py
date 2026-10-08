from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Cliente, Mecanico, Veiculo, Peca, Orcamento
from .forms import ClienteModelForm

# Create your views here.
def index(request):

    dados = Cliente.objects.all()
    context = {
        'titulo': 'Clientes',
        'dados': dados
    }
    return render(request, "index.html", context)

def Clientes(request):

    dados = Cliente.objects.all()
    context = {
        'titulo':'Mecanicos',
        'dados': dados
    }
    return render(request,"clientes.html",context)

def Mecanicos(request):

    dados = Mecanico.objects.all()
    context = {
        'titulo': 'Clientes',
        'dados': dados
    }
    return render(request, "mecanicos.html", context)

def Veiculos(request):
    dados = Veiculo.objects.all()
    context = {
        'titulo': 'Veiculos',
        'dados': dados
    }
    return render(request, "veiculos.html", context)

def Pecas(request):
    dados = Peca.objects.all()
    context = {
        'titulo': 'Peças',
        'dados': dados
    }
    return render(request, "pecas.html", context)

def Orcamentos(request):
    dados = Orcamento.objects.all()
    context = {
        'titulo': 'Orçamentos',
        'dados': dados
    }
    return render(request, "orcamentos.html", context)

def cadClientes(request):

    if request.method == "POST":
        form = ClienteModelForm(request.POST)

        if form.is_valid():
            cliente = form.save()
            form = ClienteModelForm()

            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect("clientes")
    else:
        form = ClienteModelForm()

    context = {
        'titulo': 'Clientes',
        'form': form
    }
    return render(request,"cadClientes.html", context)