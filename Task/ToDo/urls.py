from django.urls import path
from ToDo import views
urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_tarefa/', views.new_task, name ='newTask'),
    path('atualizar_tarefa/<id>', views.atualiza_tarefa, name='atualiza'),
    path('processa_form/', views.processa_form, name='processa_form'),
    path('atualiza_form/<id>', views.atualiza_form, name='atualizaForm'),
    path('delete/<id>/', views.delete, name='delete'),

]
