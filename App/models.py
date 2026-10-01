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

class Marca(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        # Na hora de preencher os dados na tela do formulario. isso faz aparecer o nome da marca escrito na tela
        return self.nome

class Veiculo(models.Model):
    # Para um sistema comercial usar o models.CASCADE garante o risco de, se uma marca for apagado todo veiculo cadastrado com a marca será apagado também
    # Usar models.PROTECT, impede a exclusão de uma marca se já houver um carro usando ela.
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    nome 
    modelo
    ano_fabricacao
    ano_modelo
    cor