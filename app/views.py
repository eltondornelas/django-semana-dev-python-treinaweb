from django.shortcuts import render, redirect
from .forms import TaskForm
from .entities.task import Task
from .services import task_service

# Create your views here.

'''
Arquitetura MVT -> Model View Template
View -> Controller

Template -> camada de View

'''


def task_list(request):
    tasks = task_service.task_list()
    # task_name = 'Assistindo a Treinaweb'

    return render(request, 'tasks/task_list.html',
                  {"tasks": tasks})

    # o último parâmetro, é como estivesse enviando
    # o contexto para o template (setAttribute() no java)


def register_task(request):
    # TODO: entender porque o erro não aparece no template

    if request.method == 'POST':
        form_task = TaskForm(request.POST)
        # o TaskForm ja valida os campos automaticamente

        if form_task.is_valid():
            title = form_task.cleaned_data['title']
            description = form_task.cleaned_data['description']
            expiration_date = form_task.cleaned_data['expiration_date']
            priority = form_task.cleaned_data['priority']
            new_task = Task(title, description,
                            expiration_date, priority)

            task_service.register_task(new_task)
            return redirect('task_list_route')
    else:
        form_task = TaskForm()

    return render(request, 'tasks/form_task.html', {"form_task": form_task})


def edit_task(request, id):
    task_db = task_service.task_list_id(id)
    form_task = TaskForm(request.POST or None, instance=task_db)
    # é como se recebesse o form preenchido do bd.
    if form_task.is_valid():
        # se possui os 4 campos válidos
        title = form_task.cleaned_data['title']
        description = form_task.cleaned_data['description']
        expiration_date = form_task.cleaned_data['expiration_date']
        priority = form_task.cleaned_data['priority']

        new_task = Task(title, description,
                        expiration_date, priority)

        task_service.edit_task(task_db, new_task)
        return redirect('task_list_route')

    return render(request, 'tasks/form_task.html', {"form_task": form_task})


def remove_task(request, id):
    task_db = task_service.task_list_id(id)
    if request.method == 'POST':
        task_service.remove_task(task_db)
        return redirect('task_list_route')

    return render(request, 'tasks/confirmation.html', {'task': task_db})
