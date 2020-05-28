from django.urls import path
from .views.task_views import *
from .views.user_views import *

urlpatterns = [
    path('task_list/', task_list, name='task_list_route'),
    path('register_task/', register_task, name='register_task_route'),
    path('edit_task/<int:id>', edit_task, name='edit_task_route'),
    path('remove_task/<int:id>', remove_task, name='remove_task_route'),
    path('register_user/', register_user, name='register_user_route'),
    path('login_user/', login_user, name='login_user_route'),
    path('logout_user/', logout_user, name='logout_user_route'),
    #           url  ,  method/class,  route
    # <tipo:nome_parametro> -> o nome tem que bater com o do método
]
