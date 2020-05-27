from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('task_list/', task_list, name='task_list_route'),
    #           url  ,  method/class,  route
]
