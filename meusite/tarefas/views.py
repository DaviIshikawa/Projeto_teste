from django.shortcuts import render
from django.http import HttpResponse

def tarefas_home(request):
    return HttpResponse("<h1>Aqui estão estão tarefas!</h1>")

def tarefas_adiconar(request):
    return HttpResponse("<h1>Adicionar Tarefa</h1>")
