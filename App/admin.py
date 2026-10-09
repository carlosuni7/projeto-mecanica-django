from django.contrib import admin

# Register your models here.

from .models import Cliente, Mecanico, Marca, Veiculo, StatusPeca, Peca, TipoVeiculo
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','cpf','telefone')

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(TipoVeiculo)
class TiposVeiculos(admin.ModelAdmin):
    list_display = ('nome',)
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa','marca','modelo', 'proprietario','tipo_veiculo', 'ano_fabricacao', 'ano_modelo', 'cor')

@admin.register(StatusPeca)
class StatusPecaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor','quantidade', 'status')