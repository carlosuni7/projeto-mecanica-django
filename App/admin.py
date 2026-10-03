from django.contrib import admin

# Register your models here.

from .models import Cliente, Mecanico, Marca, Veiculo, Peca
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','cpf','telefone')

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'cliente', 'nome', 'modelo', 'ano_fabricacao', 'ano_modelo', 'cor')

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_unitario')