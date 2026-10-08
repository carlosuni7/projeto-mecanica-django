from django import forms
from .models import Cliente, Mecanico, Marca, Veiculo, Peca

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','email','cpf','telefone']
        labels = {
            'nome': 'Nome Completo*',
            'email': 'E-mail*',
            'cpf': 'CPF*',
            'telefone': 'Celular / WhatsApp*'
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'class':'','placeholder': 'Digite o nome do cliente'}),
            'email': forms.TextInput(attrs={
                'class':'','placeholder':'@gmail.com'}),
            'cpf': forms.TextInput(attrs={
                'class':'','placeholder':'Digite o CPF do cliente'}),
            'telefone': forms.TextInput(attrs={
                'class':'', 'placeholder':'(18) 00000-0000'}),
        }


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