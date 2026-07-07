from django.http import HttpResponse

def teste_view(repost):
    return HttpResponse("<h1>Olá, mundo! Esta é uma view de teste.</h1>")

def index_view(request):
    return HttpResponse("<h1>Bem-vindo à página inicial!</h1><p style='color: blue;'>Agora meu sistema está em desenvolvimento.</p>")

def admin_view(request):
    return HttpResponse("<h1>Area de administração.</h1>")