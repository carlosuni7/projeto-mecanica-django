from django import forms
from .models import Cliente, Mecanico, Marca, Veiculo, Peca

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','email','cpf','telefone']


class MecanicoModelForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ['nome','cpf','telefone']

class MarcaModelForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']

class VeiculoModelForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'cliente','nome', 'modelo', 'ano_fabricacao', 'ano_modelo', 'cor']


class PecaModelForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome','valor_unitario']