from django.shortcuts import render

from django.contrib import messages
from .models import Cliente
from .forms import ClienteModelForm

# Create your views here.
def index(request):

    dados = Cliente.objects.all()
    context = {
        'titulo': 'Clientes',
        'dados': dados
    }
    return render(request, "index.html", context)


def cadClientes(request):

    dados = Cliente.objects.all()
    context = {
        'titulo': 'Clientes',
        'dados': dados
    }
    return render(request,"cadClientes.html", context)