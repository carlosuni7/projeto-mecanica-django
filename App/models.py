from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False, 
    help_text='insira seu nome',
    verbose_name="Nome Completo"
    )
    email = models.CharField(max_length=100, blank=False, null=False,
    help_text='insira seu email',
    verbose_name="Email"
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF"
    )
    telefone = models.CharField(
        max_length=11, blank=True,null=True,
        help_text="insira seu telefone",
        verbose_name="Telefone"
    )

    def __str__(self):
        return self.nome
    
    
class Mecanico(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False, 
        help_text='insira seu nome',
        verbose_name="Nome Mecânico"
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF"
    )
    telefone = models.CharField(
        max_length=11, blank=True,null=True,
        help_text="insira seu telefone",
        verbose_name="Telefone"
    )

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        # Na hora de preencher os dados na tela do formulario. 
        # isso faz aparecer o nome da marca escrito na tela
        return self.nome

class TipoVeiculo(models.Model):
    nome = models.CharField(max_length=40, unique=True, null=False, blank=False,
                            verbose_name="Tipo do veiculo")

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    placa = models.CharField(
            max_length=100, null=False, blank=False,
            verbose_name="Placa"
            )
    # Para um sistema comercial usar o models.CASCADE garante o risco de, se uma marca for apagado todo veiculo cadastrado com a marca será apagado também
    # Usar models.PROTECT, impede a exclusão de uma marca se já houver um carro usando ela.
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

    modelo = models.CharField(
            max_length=200, null=False, blank=False,
            verbose_name="Modelo"
            )
    proprietario = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo_veiculo = models.ForeignKey(TipoVeiculo, on_delete=models.PROTECT)

    ano_fabricacao = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Ano de Fabricação"
        )
    # O positive integer impede que seja inserido um valor negativo no campo
    ano_modelo = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Ano de Modelo"
    )
    cor = models.CharField(
        max_length=80, null=False, blank=False,
        verbose_name="Cor"
        )

    def __str__(self):
        return f"{self.placa} {self.proprietario} - {self.marca} - {self.modelo}"

class StatusPeca(models.Model):
    descricao = models.CharField(max_length=40,null=False, blank=False,verbose_name="Descrição do status")

    def __str__(self):
        return self.descricao
class Peca(models.Model):

    nome = models.CharField(
        max_length=200, null=False, blank=False,
        verbose_name="Nome Peça")
    
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00,blank=False,
        verbose_name="Preço Unitário")
    # o parametro validators me permitir cria um valor minimo que deve ser inserido ao campo da model, junto com uma mensagem de erro, caso insira um valor menor que o definido. MUITO BOM
    #  o parametro localize=false impede que o ano seja renderizado como "ex: 2.026".
    quantidade = models.IntegerField(null=False, blank=False,default=0,validators=[MinValueValidator(0,"A quantidade de peças deve ser maior que zero ( 0 )")])

    status = models.ForeignKey(StatusPeca, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} - {self.status}"

# class Servico(models.Model):
#     nome = models.CharField(
#         max_length=100, null=False, blank=False,
#         verbose_name="Serviço")
#     valor = models.DecimalField(
#         max_digits=8, decimal_places=2, default=0.00,
#         verbose_name="Valor Serviço")

#     def __str__(self):
#         return self.nome

class StatusOrcamento(models.Model):
    descricao = models.CharField(
        max_length=100, null=False, blank=False
    )
    def __str__(self):
        return self.descricao

class Orcamento(models.Model):

    # ORM (Mapeamento Objeto-Relacional) do Django
    # na coluna veiculo eu recupero todos os dados da tabela veiculos como um objeto
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)

    # Salva a data/hora atual apenas na criação do registro
    # data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=False, time)
    # preenche o campo com a data atual por padrão, mas manter a possibilidade de o usuário alterar essa data no sistema
    data_criacao = models.DateField(default=timezone.now)
    status = models.ForeignKey(StatusOrcamento, on_delete=models.PROTECT, null=True, blank=True)
    # Relações N:M apontando para as tabelas intermediárias
    pecas = models.ManyToManyField(Peca, through='OrcamentoPeca')
    # servico = models.ForeignKey(OrcamentoServico, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
            return f"{self.veiculo} - {self.veiculo.proprietario} - {self.status}"

class OrcamentoPeca(models.Model):

    # Relações N:M apontando para as tabelas intermediárias
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)

    quantidade = models.PositiveIntegerField()
    valor_cobrado = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.peca.nome} - {self.orcamento.veiculo.modelo} - {self.orcamento.status}"

# class OrcamentoServico(models.Model):

#     # Relações N:M apontando para as tabelas intermediárias
#     orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
#     servico = models.ManyToManyField(Peca, through="OrcamentoServico")
#     valor_cobrado = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)



