from django.shortcuts import render, redirect

from .models import Livro, Reserva, Emprestimo, Categoria
from usuario.models import Usuario
from leitor.models import Leitor

# Create your views here.

# CRUD LIVROS E CATEGORIAS

def livros(request):
    if request.method == 'GET':

        return render(request, 'livros.html', {
            'categorias': Categoria.objects.all(),
            'livros': Livro.objects.all()
        })
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        co_autor = request.POST.get('co_autor')
        n_paginas = request.POST.get('n_paginas')
        editora = request.POST.get('editora')
        categoria = request.POST.get('categoria')
        isbn = request.POST.get('isbn')
        estado = request.POST.get('estado')

        if titulo.strip() and autor.strip() and categoria.strip() and n_paginas.strip() and isbn.strip() and estado.strip() and editora.strip():
            categoria = Categoria.objects.get(id=categoria)
            Livro(titulo=titulo, autor=autor, co_autor=co_autor, n_paginas=n_paginas, categoria=categoria, isbn=isbn, estado=estado, editora=editora).save()

    return render(request, 'livros.html', {
        'categorias': Categoria.objects.all(),
        'livros': Livro.objects.all()
    })


def add_categorias(request):
    if request.method == 'GET':
        return render(request, 'livros.html', {
            'categorias': Categoria.objects.all(),
            'livros': Livro.objects.all()
        })
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    if nome.strip() and descricao.strip():
        Categoria(nome=nome, descricao=descricao).save()
        return render(request, 'livros.html', {
            'categorias': Categoria.objects.all(),
            'livros': Livro.objects.all()
        })
    return redirect('dashboard')


def delete_livro(request, id):
    if request.method == 'POST':
        livro = Livro.objects.get(id=id)
        livro.delete()
    return redirect('dashboard')

def delete_categoria(request, id):
    if request.method == 'POST':
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
    return redirect('dashboard')


def update_livro(request, id):
    if request.method == 'POST':
        livro = Livro.objects.get(id=id)
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        co_autor = request.POST.get('co_autor')
        n_paginas = request.POST.get('n_paginas')
        editora = request.POST.get('editora')
        categoria = request.POST.get('categoria')
        isbn = request.POST.get('isbn')
        estado = request.POST.get('estado')

        if titulo.strip() and autor.strip() and categoria.strip() and n_paginas.strip() and isbn.strip() and estado.strip() and editora.strip():
            categoria = Categoria.objects.get(id=categoria)
            livro.titulo = titulo
            livro.autor = autor
            livro.co_autor = co_autor
            livro.n_paginas = n_paginas
            livro.categoria = categoria
            livro.isbn = isbn
            livro.estado = estado
            livro.editora = editora
            livro.save()
    return redirect('dashboard')


def update_categoria(request, id):
    if request.method == 'POST':
        categoria = Categoria.objects.get(id=id)
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        if nome.strip() and descricao.strip():
            categoria.nome = nome
            categoria.descricao = descricao
            categoria.save()
    return redirect('livros')

#  RESERVAS 

def reservas(request):
    if request.method == 'GET':
        return render(request, 'reservas.html', {
            'reservas': Reserva.objects.all()
        })

def reservar_livro(request, id):
    if request.method == 'POST':
        livro = Livro.objects.get(id=id)
        usuario = Usuario.objects.get(id=request.session['usuario_id'])
        leitor = Leitor.objects.get(id=request.POST.get('leitor'))
        Reserva(livro=livro, usuario=usuario, leitor=leitor).save()
    return redirect('livros')

def deletar_reserva(request, id):
    if request.method == 'POST':
        reserva = Reserva.objects.get(id=id)
        reserva.delete()
    return redirect('livros')

def update_reserva(request, id):
    if request.method == 'POST':
        reserva = Reserva.objects.get(id=id)
        livro = Livro.objects.get(id=request.POST.get('livro'))
        usuario = Usuario.objects.get(id=request.session['usuario_id'])
        leitor = Leitor.objects.get(id=request.POST.get('leitor'))
        reserva.livro = livro
        reserva.usuario = usuario
        reserva.leitor = leitor
        reserva.save()
    return redirect('livros')

# EMPRESTIMOS

def emprestimos(request):
    if request.method == 'GET':
        return render(request, 'emprestimos.html', {
            'emprestimos': Emprestimo.objects.all()
        })

def emprestar_livro(request, id):
    if request.method == 'POST':
        livro = Livro.objects.get(id=id)
        usuario = Usuario.objects.get(id=request.session['usuario_id'])
        leitor = Leitor.objects.get(id=request.POST.get('leitor'))
        Emprestimo(livro=livro, usuario=usuario, leitor=leitor).save()
    return redirect('emprestimo')


def deletar_emprestimo(request, id):
    if request.method == 'POST':
        emprestimo = Emprestimo.objects.get(id=id)
        emprestimo.delete()
    return redirect('emprestimo')

def update_emprestimo(request, id):
    if request.method == 'POST':
        emprestimo = Emprestimo.objects.get(id=id)
        livro = Livro.objects.get(id=request.POST.get('livro'))
        usuario = Usuario.objects.get(id=request.session['usuario_id'])
        leitor = Leitor.objects.get(id=request.POST.get('leitor'))
        emprestimo.livro = livro
        emprestimo.usuario = usuario
        emprestimo.leitor = leitor
        emprestimo.save()
    return redirect('emprestimo')