from django.shortcuts import render

# Create your views here.

'''
Arquitetura AMTV
View -> Controller

Template -> camada de View

'''


def task_list(request):
    task_name = 'Assistindo a Treinaweb'
    return render(request, 'tasks/task_list.html',
                  {"task_name": task_name})
