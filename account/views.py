from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home:main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home:main')
    return render(request, 'account/login.html', context={})


def logout_user(request):
    logout(request)
    return redirect('home:main')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home:main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm = request.POST.get('confirm')
            if username and email and password and confirm:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect('home:main')

    return render(request, 'account/register.html', context={})


def display(request, ID):
    user = User.objects.get(id=ID)
    return render(request, 'account/display.html', context={'user': user})


#def profile(request, pk)