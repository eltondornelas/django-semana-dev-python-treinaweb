from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import TaskForm
from app.entities.task import Task
from ..services import task_service


# com o @login_required é um decorator que verifica se usuário esta logado
# se não estiver ele é redirecionado
# perceba que a página padrão é o account/login; para ajustar isso deve ir em
# settings.py e criar LOGIN_URL

@login_required()
def task_list(request):
    tasks = task_service.task_list(request.user)
    # request.user é o usuário logado

    return render(request, 'tasks/task_list.html',
                  {"tasks": tasks})


@login_required()
def register_task(request):
    if request.method == 'POST':
        form_task = TaskForm(request.POST)
        # o TaskForm ja valida os campos automaticamente

        if form_task.is_valid():
            title = form_task.cleaned_data['title']
            description = form_task.cleaned_data['description']
            expiration_date = form_task.cleaned_data['expiration_date']
            priority = form_task.cleaned_data['priority']
            new_task = Task(title, description,
                            expiration_date, priority, request.user)

            task_service.register_task(new_task)
            return redirect('task_list_route')
    else:
        form_task = TaskForm()

    return render(request, 'tasks/form_task.html', {"form_task": form_task})


@login_required()
def edit_task(request, id):
    task_db = task_service.task_list_id(id)

    if task_db.user != request.user:
        return HttpResponse('Não Permitido!')

    form_task = TaskForm(request.POST or None, instance=task_db)

    if form_task.is_valid():
        title = form_task.cleaned_data['title']
        description = form_task.cleaned_data['description']
        expiration_date = form_task.cleaned_data['expiration_date']
        priority = form_task.cleaned_data['priority']

        new_task = Task(title, description,
                        expiration_date, priority, request.user)

        task_service.edit_task(task_db, new_task)
        return redirect('task_list_route')

    return render(request, 'tasks/form_task.html', {"form_task": form_task})


@login_required()
def remove_task(request, id):
    task_db = task_service.task_list_id(id)

    if task_db.user != request.user:
        return HttpResponse('Não Permitido!')

    if request.method == 'POST':
        task_service.remove_task(task_db)
        return redirect('task_list_route')

    return render(request, 'tasks/confirmation.html', {'task': task_db})
