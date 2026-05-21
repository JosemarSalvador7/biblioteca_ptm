from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from livro.models import Livro, Emprestimo, Reserva, Categoria
import hashlib
import re

# Create your views here.

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        senha = request.POST.get('senha')
        if (name == '') or (senha == ''):
            return redirect('login')
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario = Usuario.objects.filter(nome=name, senha=senha)
        if not usuario.exists():
            request.session['tentativas'] = request.session['tentativas'] + 1
            return redirect(f'/auth/login/?status=0&tentativa={request.session['tentativas']}')
        request.session['usuario'] = usuario[0].id  # type: ignore
        request.session['nivel_acesso'] = usuario[0].nivel_acesso
        request.session['tentativas'] = 0
        return redirect('dashboard')
    if request.session.get('tentativas') is None or request.session.get('tentativas') == '':
        request.session['tentativas'] = 0
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status,'tentativa':request.session['tentativas']})

def recuperar_senha1(requets):
    if requets.method == 'POST':
        nome = requets.POST.get('name')
        senha_rec = requets.POST.get('senha_rec')
        bi = requets.POST.get('bi')
            
        if (nome == '') or (bi == '') or (senha_rec == ''):
            return redirect('/auth/recuperar_senha_um/?status=0')
        
        senha_rec = hashlib.sha256(senha_rec.encode()).hexdigest()
        usuario = Usuario.objects.filter(nome=nome, senha_rec=senha_rec, bi=bi)
        if not usuario.exists():
            return redirect('/auth/recuperar_senha_um/?status=0')
        else:
            return render(requets,'edi_senha.html',{'usuario_id':usuario[0].id}) #type: ignore
    
    return render(requets, 'recuperacao.html',{})  # type: ignore

def recuperar_senha2(requets):
    if requets.method == 'POST':
        nome = requets.POST.get('name')
        senha_rec = requets.POST.get('senha_rec')
        bi = requets.POST.get('bi')
            
        if (nome == '') or (bi == '') or (senha_rec == ''):
            return redirect('/auth/recuperar_senha_um/?status=0')
        
        senha_rec = hashlib.sha256(senha_rec.encode()).hexdigest()
        usuario = Usuario.objects.filter(nome=nome, senha_rec2=senha_rec, bi=bi)
        if not usuario.exists():
            return redirect('/auth/recuperar_senha_um/?status=0')
        else:
            return render(requets,'edi_senha.html',{'usuario_id':usuario[0].id}) #type: ignore
    return render(requets, 'recuperacao2.html',{})  
    






def alterar_senha(requests,id):
    if requests.method == 'POST':    
        senha_nova = requests.POST.get('senha_nova')
        senha_nova = hashlib.sha256(senha_nova.encode()).hexdigest()
        usuario = Usuario.objects.get(id=id)
        usuario.senha = senha_nova
        usuario.save()        
        return redirect('/auth/login/?status=22')

def cadastro_user(request):    
    if request.method != 'POST':
        return redirect('login')
    name = request.POST.get('name')
    senha = request.POST.get('senha')
    bi = request.POST.get('bi')
    senha_rec = request.POST.get('senha_rec')
    senha_rec2 = request.POST.get('senha_rec2')

    # nenhum dado deve ser vazio
    if (name == '') or (senha == '') or (bi == '') or (senha_rec == '') or (senha_rec2 == ''):
        return redirect('login')
    # nenhuma das senhas deve ser igual
    if (senha == senha_rec) or (senha == senha_rec2) or (senha_rec == senha_rec2):
        return redirect('login')
    if not re.fullmatch(re.compile(r'[A-Za-z0-9]+'), name):
        return redirect('login')
    senha = hashlib.sha256(senha.encode()).hexdigest()
    senha_rec = hashlib.sha256(senha_rec.encode()).hexdigest()
    senha_rec2 = hashlib.sha256(senha_rec2.encode()).hexdigest()
    Usuario(name, senha, bi, senha_rec, senha_rec2, senha).save()

    return redirect('home')


def dashboard(request):
    if not request.session.get('usuario'):
        return redirect('login')
    Total_livros = Livro.objects.count()
    usuario = Usuario.objects.get(id=request.session.get('usuario'))
    categorias = Categoria.objects.all()

    return render(request, 'dashboard.html', {'usuario': usuario,
                                              'nivel_acesso': request.session.get('nivel_acesso'),
                                              'total_livros': Total_livros,
                                              'categorias': categorias.count(),
                                              })


def landing(requets):
    return render(requets,'landing.html',{})

def logout(request):
    request.session.flush()
    return redirect('login')
