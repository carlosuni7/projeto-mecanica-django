from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Cliente, Mecanico, Veiculo, Peca, Orcamento, StatusOrcamento, OrcamentoPeca
from .forms import ClienteModelForm, MecanicoModelForm, PecaModelForm, VeiculoModelForm, OrcamentoModelForm

tables = {
    'mecanico' : {
        'titulo':'Mecanicos',
        'nome': 'mecanico',
        'url':'mecanicos',
        'model': Mecanico,
        'form': MecanicoModelForm
    },
    'peca' : {
        'titulo':'Peças',
        'nome': 'peca',
        'url': 'pecas',
        'model': Peca,
        'form':PecaModelForm
    }
}

nav = [
        {'text':'Visão Geral','url':'dashboard','icone':'layout-dashboard.svg',},
        {'text':'Clientes','url':'clientes','icone':'users.svg',},
        {'text':'Mecanicos','url':'mecanicos','icone':'user-round-cog.svg'},
        {'text':'Veiculos','url':'veiculos','icone':'car-front.svg',},
        {'text':'Peças','url':'pecas','icone':'package.svg',},
        {'text':'Orçamentos','url':'orcamentos','icone':'file-text.svg',},
    ]


def ExcluirRegistro(request, tabela, pk):
    registro = tables.get(tabela)
    
    model = registro['model'].objects.get(id=pk)
    if registro['model'] is None:
        return redirect('error')

    if request.method == 'POST':
        model.delete()
        return redirect(registro['url'])
    
    context = {
        'titulo':registro['titulo'],
        'tabela':registro['nome'],
        'descricao':'Confira os dados do registro antes de confirmar a exclusão.',
        "registro": model
    }
    
    return render(request, "excluir.html", context)

def Erro(request):
    context = {
        'titulo': 'Pagina de Error 404'
    }
    return render(request, "error.html",context)

# Create your views here.
def index(request):
    context = {
        'titulo': 'Bem-Vindo',
    }
    return render(request, "index.html", context)

def Dash(request, nav = nav):

    context = {
        'titulo': 'Dashboard',
        'navegacao': nav
    }
    return render(request,"dashboard.html", context)
# CRUD DE CLIENTES
def Clientes(request, nav = nav):

    dados = Cliente.objects.all()
    context = {
        'titulo':'Clientes',
        'dados': dados,
        'navegacao': nav
    }
    return render(request,"cliente/gerenciamento.html",context)

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
        "titulo":"cliente",
        'descricao':'Confira os dados do cliente antes de confirmar a exclusão.',
        "registro": cliente
    }

    return render(request, "cliente/excluir.html", context)

# CRUD DE MECANICOS
def Mecanicos(request, nav = nav):
    
    mecanicos = Mecanico.objects.all()
    context = {
        'titulo': 'Mecanicos',
        'mecanicos': mecanicos,
        'navegacao': nav
    }
    return render(request, "mecanico/gerenciamento.html", context)

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

def exMecanico(request, pk):

    mecanico = Mecanico.objects.get(id=pk)
    #print(contato)
    if request.method == 'POST':
        #form = ContatoModelForm(request.POST)
        #if form.is_valid():
            mecanico.delete()
            return redirect("mecanicos")

    context = {
        "titulo":"mecanico",
        'descricao':'Confira os dados do mecânico antes de confirmar a exclusão.',
        "registro": mecanico
    }

    return render(request, "mecanico/excluir.html", context)

# CRUD DE VEICULOS
def Veiculos(request, nav = nav):
    
    dados = Veiculo.objects.all()
    context = {
        'titulo': 'Veiculos',
        'dados': dados,
        'navegacao': nav,
    }
    return render(request, "veiculo/gerenciamento.html", context)

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
            "titulo":"veiculo",
            'descricao':'Confira os dados do veículo antes de confirmar a exclusão.',
            "registro": veiculo
    }

    return render(request, "veiculo/excluir.html", context)

# CRUD DE PEÇAS
def Pecas(request, nav = nav):
    dados = Peca.objects.all()
    context = {
        'titulo': 'Peças',
        'dados': dados,
        'navegacao': nav
    }
    return render(request, "peca/gerenciamento.html", context)

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
                "titulo":"peca",
                'descricao':'Confira os dados da peça antes de confirmar a exclusão.',
                "registro": peca
        }

    return render(request, "peca/excluir.html", context)

# CRUD DE ORÇAMENTOS
def Orcamentos(request, nav = nav):
    orcamentos = OrcamentoPeca.objects.all()
    context = {
        'titulo': 'Orçamentos',
        'orcamentos': orcamentos,
        'navegacao': nav
    }
    return render(request, "orcamento/gerenciamento.html", context)

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

def exOrcamento(request, pk):

    orcamento = Orcamento.objects.get(id=pk)
    #print(contato)
    if request.method == 'POST':
        #form = ContatoModelForm(request.POST)
        #if form.is_valid():
            orcamento.delete()
            return redirect("orcamentos")

    context = {
                "titulo":"orcamento",
                'descricao':'Confira os dados do orçamento antes de confirmar a exclusão.',
                "registro": orcamento
        }

    return render(request, "orcamento/excluir.html", context)