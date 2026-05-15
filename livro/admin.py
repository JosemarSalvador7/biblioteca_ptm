from django.contrib import admin

from livro.models import Categoria, Emprestimo, Livro,Reserva

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Reserva)