from django.contrib import admin
from .models import Avalicacao,Curso


# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo','url','publicacao','atualizacao','ativo')
 
    
@admin.register(Avalicacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso','nome','email','avaliacao','publicacao','atualizacao','ativo')