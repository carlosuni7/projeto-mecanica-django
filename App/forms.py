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
        # Usar o widgets me permite estilizar de forma mais personalizada cada input e label do formulario de acordo com cada fields
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
        fields = ['placa','marca','modelo', 'proprietario', 'tipo_veiculo', 'ano_fabricacao', 'ano_modelo', 'cor']
        labels = {
                    'placa': 'Placa*',
                    'marca': 'Marca*',
                    'modelo': 'Modelo*',
                    'proprietario': 'Proprietario*',
                    'tipo_veiculo': 'Tipo Veiculo*',
                    'ano_fabricacao':'Ano de Fabricação*',
                    'ano_modelo': 'Ano de Modelo*',
                    'cor': 'Cor*'
                }
        widgets = {
                    'placa': forms.TextInput(attrs={'class':'','placeholder': 'Digite placa do veiculo'}),
                    'modelo': forms.TextInput(attrs={'class':'','placeholder': 'Modelo do veiculo'}),
                    'cor': forms.TextInput(attrs={'class':'','placeholder': 'Digite cor do veiculo'}),
                    'proprietario': forms.Select(attrs={'class':''}),
                    'marca': forms.Select(attrs={'class':''}),
                    'tipo_veiculo': forms.Select(attrs={'class':''}),
                    'ano_fabricacao': forms.NumberInput(attrs={'class':'','placeholder': 'Ano de fabricação'}),
                    'ano_modelo': forms.NumberInput(attrs={'class':'','placeholder': 'Ano de modelo'}),
                    
                    
                }

class PecaModelForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome','valor', 'quantidade', 'status']