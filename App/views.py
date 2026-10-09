from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Cliente, Mecanico, Veiculo, Peca
from .forms import ClienteModelForm, MecanicoModelForm, PecaModelForm, VeiculoModelForm

# Create your views here.
def index(request):

    dados = Cliente.objects.all()
    context = {
        'titulo': 'Clientes',
        'dados': dados
    }
    return render(request, "index.html", context)

def Dash(request):

    context = {
        'titulo': 'Dashboard'
    }
    return render(request,"dashboard.html", context)
# CRUD DE CLIENTES
def Clientes(request):

    dados = Cliente.objects.all()
    context = {
        'titulo':'Clientes',
        'dados': dados
    }
    return render(request,"cliente/clientes.html",context)

def cadClientes(request):

    if request.method == "POST":
        form = ClienteModelForm(request.POST)

        if form.is_valid():
            cliente = form.save()
            form = ClienteModelForm()

            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect("clientes")
        else:
            messages.error(request, 'Erro ao cadastrar contato')
    else:
        form = ClienteModelForm()

    context = {
        'titulo': 'Clientes',
        'form': form
    }
    return render(request,"cliente/cadastrar.html", context)

def altCliente(request, pk):

    cliente = Cliente.objects.get(id=pk)

    if request.method == 'POST':
        form = ClienteModelForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes")
        else:
            messages.error(request, 'Erro ao alterar veículo.')
    else:
        form = ClienteModelForm(instance=cliente)
    context = {
        "form": form,
        "cliente": cliente
    }
    return render(request, "cliente/alterar.html", context)

def exCliente(request, pk):

    cliente = Cliente.objects.get(id=pk)
    #print(contato)
    if request.method == 'POST':
        #form = ContatoModelForm(request.POST)
        #if form.is_valid():
            cliente.delete()
            return redirect("clientes")

    context = {
        "cliente": cliente
    }

    return render(request, "cliente/excluir.html", context)


# CRUD DE MECANICOS
def Mecanicos(request):

    dados = Mecanico.objects.all()
    context = {
        'titulo': 'Clientes',
        'dados': dados
    }
    return render(request, "mecanicos.html", context)

def cadMecanico(request):

    if request.method == "POST":
        form = MecanicoModelForm(request.POST)

        if form.is_valid():
            mecanico = form.save()
            form = MecanicoModelForm()

            messages.success(request, 'Mecanico cadastrado com sucesso!')
            return redirect("clientes")
    else:
        form = MecanicoModelForm()

    context = {
        'titulo': 'Mecanicos',
        'form': form
    }
    return render(request,"cadMecanicos.html", context)


# CRUD DE VEICULOS
def Veiculos(request):
    dados = Veiculo.objects.all()
    context = {
        'titulo': 'Veiculos',
        'dados': dados
    }
    return render(request, "veiculo/veiculos.html", context)

def cadVeiculo(request):

    if request.method == "POST":
        form = VeiculoModelForm(request.POST)

        if form.is_valid():
            veiculo = form.save()
            form = VeiculoModelForm()

            messages.success(request, 'Veiculo cadastrado com sucesso!')
            return redirect("veiculos")
        else:
            print(form.errors)
            messages.error(request, 'Erro ao cadastrar contato')
    else:
        form = VeiculoModelForm()

    context = {
        'titulo': 'Veiculos',
        'form': form
    }
    return render(request,"veiculo/cadastrar.html", context)

def altVeiculo(request, pk):

    veiculo = Veiculo.objects.get(id=pk)

    if request.method == 'POST':
        form = VeiculoModelForm(request.POST, request.FILES, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect("veiculos")
        else:
            print(form.errors)
            messages.error(request, 'Erro ao alterar veiculo')
    else:
        form = VeiculoModelForm(instance=veiculo)
    context = {
        "form": form,
        "veiculo": veiculo
    }
    return render(request, "veiculo/alterar.html", context)

def exVeiculo(request, pk):

    veiculo = Veiculo.objects.get(id=pk)
    #print(contato)
    if request.method == 'POST':
        #form = ContatoModelForm(request.POST)
        #if form.is_valid():
            veiculo.delete()
            return redirect("veiculos")

    context = {
        "veiculo": veiculo
    }

    return render(request, "veiculo/excluir.html", context)

# CRUD DE PEÇAS
def Pecas(request):
    dados = Peca.objects.all()
    context = {
        'titulo': 'Peças',
        'dados': dados
    }
    return render(request, "peca/pecas.html", context)

def cadPeca(request):

    if request.method == "POST":
        form = PecaModelForm(request.POST)

        if form.is_valid():
            peca = form.save()
            form = PecaModelForm()

            messages.success(request, 'Peça cadastrado com sucesso!')
            return redirect("pecas")
        else:
            print(form.errors)
            messages.error(request, 'Erro ao cadastrar peça')
    else:
        form = PecaModelForm()

    context = {
        'titulo': 'Peças',
        'form': form
    }
    return render(request,"peca/cadastrar.html", context)

def altPeca(request, pk):

    peca = Peca.objects.get(id=pk)

    if request.method == 'POST':
        form = PecaModelForm(request.POST, request.FILES, instance=peca)
        if form.is_valid():
            form.save()
            return redirect("pecas")
        else:
            print(form.errors)
            messages.error(request, 'Erro ao alterar veículo.')
    else:
        form = PecaModelForm(instance=peca)
    context = {
        "form": form,
        "peca": peca
    }
    return render(request, "peca/alterar.html", context)

def exPeca(request, pk):

    peca = Peca.objects.get(id=pk)
    #print(contato)
    if request.method == 'POST':
        #form = ContatoModelForm(request.POST)
        #if form.is_valid():
            peca.delete()
            return redirect("pecas")

    context = {
        "peca": peca
    }

    return render(request, "peca/excluir.html", context)


# CRUD DE ORÇAMENTOS

def Orcamentos(request):
    # dados = Orcamento.objects.all()
    context = {
        'titulo': 'Orçamentos',
        'dados': ''
    }
    return render(request, "orcamentos.html", context)

def cadOrcamento(request):

    if request.method == "POST":
        form = MecanicoModelForm(request.POST)

        if form.is_valid():
            orcamentos = form.save()
            form = MecanicoModelForm()

            messages.success(request, 'Orçamento cadastrado com sucesso!')
            return redirect("orcamentos")
    else:
        form = MecanicoModelForm()

    context = {
        'titulo': 'Orçamentos',
        'form': form
    }
    return render(request,"cadOrcamentos.html", context)