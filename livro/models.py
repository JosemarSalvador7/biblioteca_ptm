from django.db import models
from leitor.models  import Leitor
from usuario.models import Usuario
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=255,blank=False,null=False)
    descricao = models.CharField(max_length=255,blank=False,null=False)
    
class Livro(models.Model):
    titulo = models.CharField(max_length=255,blank=False,null=False)
    autor  = models.CharField(max_length=255,blank=False,null=False)
    co_autor = models.CharField(max_length=255,blank=True,null=True)
    isbn = models.IntegerField()
    n_paginas = models.IntegerField()
    editora = models.CharField(max_length=255,blank=False,null=False)
    data_publicacao = models.DateField()
    data_registro = models.DateField()
    estado = models.CharField(max_length=50 ,choices=(('disponivel','disponivel'),('indisponivel','indisponivel')))
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    

class Reserva(models.Model):
    leitor = models.ForeignKey(Leitor,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    data_reserva = models.DateField()
    
class Emprestimo(models.Model):
    leitor = models.ForeignKey(Leitor,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True,blank=True)
    data_devolucao_prevista = models.DateField()
    
    
