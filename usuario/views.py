from django.shortcuts import render ,redirect
from .models import Usuario
from livro.models import Livro, Emprestimo ,Reserva ,Categoria
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
        usuario = Usuario.objects.filter(name=name,senha=senha)
        request.session['usuario'] = usuario[0].id #type: ignore
        request.session['nivel_acesso'] = usuario[0].nivel_acesso #type: ignore
        if not usuario.exists():
            return redirect('login')
        return redirect('dashboard')

    return render(request,'login.html',{})


def cadastro_user(request):
    if request.method != 'POST':
        return redirect('login')
    name = request.POST.get('name')
    senha = request.POST.get('senha')
    bi = request.POST.get('bi')
    senha_rec =  request.POST.get('senha_rec')
    senha_rec2 =  request.POST.get('senha_rec2')
    
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
    
    Usuario(name,senha,bi,senha_rec,senha_rec2,senha).save()

    return redirect('home')

def dashboard(request):
    if not request.session.get('usuario'):
        return redirect('login')
    Total_livros = Livro.objects.count()
    usuario = Usuario.objects.get(id=request.session.get('usuario'))
    categorias = Categoria.objects.all()


    return render(request,'dashboard.html',{'usuario':usuario,
                                            'nivel_acesso':request.session.get('nivel_acesso'),
                                            'total_livros':Total_livros,
                                            'categorias':categorias.count(),
                                            })
    
def logout(request):
    request.session.flush()
    return redirect('login')