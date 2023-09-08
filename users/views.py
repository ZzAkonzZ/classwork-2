from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'users/login.html', {})
        else:
            return HttpResponse('Login error')
    else:
        return render(request, 'users/login.html', {})

def auth_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            if user is not None:
                return HttpResponse('Такой пользователь существует!')
        except User.DoesNotExist:
            User.objects.create_user(username, password=password)
            return render(request, 'users/login.html', {})


    else:
        return render(request, 'users/auth.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {})