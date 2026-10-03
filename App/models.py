from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False, 
    help_text='insira seu nome',
    verbose_name="Nome Completo"
    );
    email = models.CharField(max_length=100, blank=False, null=False,
    help_text='insira seu email',
    verbose_name="Email"
    );
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF"
    );
    telefone = models.CharField(
        max_length=11, blank=True,null=True,
        help_text="insira seu telefone",
        verbose_name="Telefone"
    );

    def __str__(self):
        return self.nome
    
    
class Mecanico(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False, 
        help_text='insira seu nome',
        verbose_name="Nome Mecânico"
    );
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF"
    );
    telefone = models.CharField(
        max_length=11, blank=True,null=True,
        help_text="insira seu telefone",
        verbose_name="Telefone"
    );

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        # Na hora de preencher os dados na tela do formulario. 
        # isso faz aparecer o nome da marca escrito na tela
        return self.nome

class Veiculo(models.Model):
    # Para um sistema comercial usar o models.CASCADE garante o risco de, se uma marca for apagado todo veiculo cadastrado com a marca será apagado também
    # Usar models.PROTECT, impede a exclusão de uma marca se já houver um carro usando ela.
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    nome = models.CharField(
        max_length=100, null=False, blank=False,
        verbose_name="Nome Veiculo"
        )
    modelo = models.CharField(
        max_length=200, null=False, blank=False,
        verbose_name="Modelo"
        )
    ano_fabricacao = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Ano de Fabricação"
        )
    ano_modelo = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Ano Modelo"
    )
    cor = models.CharField(
        max_length=80, null=False, blank=False,
        verbose_name="Cor veiculo"
        )

    def __str__(self):
        return f"{self.nome} - {self.marca} - {self.modelo}"

class Peca(models.Model):

    nome = models.CharField(
        max_length=200, null=False, blank=False,
        verbose_name="Nome Peça")
    
    valor_unitario = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00,
        verbose_name="Preço Unitário")

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(
        max_length=100, null=False, blank=False,
        verbose_name="Serviço")
    valor = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00,
        verbose_name="Valor Serviço")

    def __str__(self):
        return self.nome

class Orcamento(models.Model):

    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)

    data = models.DateField(verbose_name="Data Orçamento")

class OrcamentoPeca(models.Model):

    orcamento = models.ForeignKey(Orcamento, on_delete=models.PROTECT)
    peca = models.ForeignKey(Peca, on_delete=models.PROTECT)

    quantidade = models.PositiveIntegerField()
    valor_cobrado = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)


class OrcamentoServico(models.Model):

    orcamento = models.ForeignKey(Orcamento, on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)


# table mecanico_servico {
#   id_mecanico_servico int [pk, not null]

#   id_mecanico int  [Ref: > mecanico.id_mecanico]
#   id_servico int [Ref: > servicos.id_servico]
#   data date
# }