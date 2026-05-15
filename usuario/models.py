from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    bi = models.CharField(max_length=14)
    senha = models.CharField(max_length=64)
    senha_rec = models.CharField(max_length=64)
    senha_rec2 = models.CharField(max_length=64)
    data_registro =  models.DateField()
    nivel_acesso = models.CharField(max_length=1,choices=(('B','bibliotecário'),('A','Administrador')))
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    
