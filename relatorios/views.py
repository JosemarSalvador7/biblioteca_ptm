from django.shortcuts import render
from leitor.models import Leitor
from livro.models import Livro, Reserva, Emprestimo, Categoria
from usuario.models import Usuario

# Create your views here.


def relatorios(request):
    if request.method == 'GET':
        return render(request, 'relatorios.html', {
            'leitores': Leitor.objects.all(),
            'emprestimos': Emprestimo.objects.all(),
            'reservas': Reserva.objects.all(),
            'livros': Livro.objects.all(),
            'categorias': Categoria.objects.all(),
            'usuarios': Usuario.objects.all()
        })
        
    if request.method == 'POST':
        return render(request, 'relatorios.html', {
            'leitores': Leitor.objects.all(),
            'emprestimos': Emprestimo.objects.all(),
            'reservas': Reserva.objects.all(),
            'livros': Livro.objects.all(),
            'categorias': Categoria.objects.all(),
            'usuarios': Usuario.objects.all()
        })
