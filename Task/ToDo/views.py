from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse

from ToDo.models import Task


# Create your views here.

def index(request): # pagina principal
    task_list = Task.objects.all()
    pesquisa = request.GET.get('pesquisa') or ''
    if pesquisa:
        task_list = Task.objects.filter(name__startswith=pesquisa)

    return render(request, 'ToDo/index.html', {
        'task' : task_list,
        'pesquisa' : pesquisa
    })

def new_task(request): #pagina  para criar tarefa
    return render(request, 'ToDo/adicionar_tarefa.html')

def atualiza_tarefa(request, id): # pagina para atualizar tarefa
    task = get_object_or_404(Task, pk=id)
    return render(request,'ToDo/atualizar_tarefa.html', {
        'task':task.name,
        'descript':task.description,
        'status':task.status,
        'id': task.id
    })

def processa_form(request): # recebe o form de criar tarefa e cria uma nova tarefa no banco
    nome = request.POST.get('nome')
    descrip = request.POST.get('descript')
    
    task = Task(name=nome, description = descrip)
    task.save()

    return redirect('index')

def atualiza_form(request, id): # atualiza uma tarefa já existênte
    try:
        task = get_object_or_404(Task, pk=id)

        nome = request.POST.get('nome')
        descrip = request.POST.get('descript')
        status = request.POST.get('status')
        if status == 'Realizada':
            status = 'E'
        else:
            status = 'O'
        task.name = nome
        task.description = descrip
        task.status = status
        task.save()
        return redirect('index')
    except Exception as error:
        return HttpResponse(error)

def delete(request, id): # deleta uma tarefa
    try:
        task = get_object_or_404(Task, pk=id)
        task.delete()
        return redirect('index')
    except Exception as error:
        return HttpResponse(error)