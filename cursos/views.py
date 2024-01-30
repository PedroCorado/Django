from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

def acessar_curso(request):
    return render(request, 'acessar_curso.html')
def criar_curso(request):
    if request.method == 'GET':
        return render(request, 'criar_curso.html')
    elif request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        carga_horaria_digitada = request.POST.get('carga_horaria')
        
        curso = Curso(
            nome=nome_digitado,
            carga_horaria=carga_horaria_digitada,
            data_criacao=datetime.now(),
        )
        curso.save()
        return redirect('/curso/criar_curso')