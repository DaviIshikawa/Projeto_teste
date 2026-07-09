from django.urls import path
from . import views

app_name= "tarefas"
urlpatterns = [
    path('', views.tarefas_home, name='home'),
    path('tarefas/adicionar/', views.tarefas_adicionar, name='adicionar'),
    path('tarefas/remover/', views.tarefas_remover, name='remover'),
    path('tarefas/editar/', views.tarefas_editar, name='editar'),
]