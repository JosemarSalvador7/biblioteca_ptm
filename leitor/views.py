from django.shortcuts import render
from leitor.models import Leitor
import re

# Create your views here.

def leitores(request):
    if request.method == 'GET':
        return render(request, 'leitores.html', {
            'leitores': Leitor.objects.all()
        })
        
    nome = request.POST.get('nome')
    bi = request.POST.get('bi')
    numero = request.POST.get('numero')
    numero_alter = request.POST.get('numero_alter')

    if not nome.strip() or not bi.strip() or not numero or not numero_alter.strip():
        return render(request, 'leitores.html', {
            'leitores': Leitor.objects.all(),
            'error': 'Todos os campos são obrigatórios'
        })
    if not re.match(r'^[0-9]{9}[A-Z]{2}[0-9]{3}$', bi):
        return render(request, 'leitores.html', {
            'leitores': Leitor.objects.all(),
            'error': 'BI inválido'
        })
    if not re.match(r'^[0-9]{9}$', numero):
        return render(request, 'leitores.html', {
            'leitores': Leitor.objects.all(),
            'error': 'Número inválido'
        })
    if not re.match(r'^[0-9]{9}$', numero_alter):   
        return render(request, 'leitores.html', {
            'leitores': Leitor.objects.all(),
            'error': 'Número alternativo inválido'
        })
    return render(request, 'leitores.html', {})

