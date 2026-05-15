from django.db import models

# Create your models here.



class Leitor(models.Model):
    nome = models.CharField(max_length=255,blank=False,null=False)
    bi = models.CharField(max_length=14)
    numero = models.IntegerField()
    numero_alter = models.IntegerField()
    estado = models.CharField(max_length=1,choices=(('A','ativo'),('B','bloqueado')),default='A')
    
    
    
    
    
    
    