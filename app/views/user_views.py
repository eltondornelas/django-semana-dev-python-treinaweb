from contextlib import redirect_stderr

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_user(request):
    # de início será uma requisição GET, logo pula para o else que cria um form
    # em branco. POST sempre vai ser quando for submetido algum formulário
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('task_list_route')
    else:
        form_user = UserCreationForm()

    return render(request, 'users/form_user.html', {"form_user": form_user})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # esse método procura no bd e traz o usuário ou None

        if user is not None:
            login(request, user)
            return redirect('task_list_route')

        else:
            messages.error(request,
                           'As credencias do usuário estão incorretas')
            return redirect('login_user_route')
    else:
        form_login = AuthenticationForm()

    return render(request, 'users/login.html', {'form_login': form_login})


def logout_user(request):
    logout(request)
    return redirect('login_user_route')
