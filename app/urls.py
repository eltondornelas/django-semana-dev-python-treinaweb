from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('task_list/', task_list, name='task_list_route'),
    path('register_task/', register_task, name='register_task_route'),
    path('edit_task/<int:id>', edit_task, name='edit_task_route'),
    path('remove_task/<int:id>', remove_task, name='remove_task_route'),
    #           url  ,  method/class,  route
    # <tipo:nome_parametro> -> o nome tem que bater com o do método
]
