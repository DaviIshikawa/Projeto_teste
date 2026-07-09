from django.shortcuts import render

def tarefas_home(request):
    contexto = {
        'nome': 'Davi'
    }
    return render(request, 'pagetarefas/home.html', contexto)

def tarefas_adicionar(request):
    return render(request, 'pagetarefas/adicionar.html')

def tarefas_remover(request):
    return render(request, 'pagetarefas/remover.html')

def tarefas_editar(request):
    return render(request, 'pagetarefas/editar.html')
