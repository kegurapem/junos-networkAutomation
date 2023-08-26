from django.shortcuts import render, redirect
from proyectnornir.tasks.main import serialize_results_to_json  # Importa la función saludo desde saludo.py
from funcionesnornir.create_hosts import create_hosts_yaml
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login


# def signup(request):

#     if request.method == 'GET':
#         return render(request, 'signup.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             # register user
#             try:
#                 user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return HttpResponse('User created successfully')
#             except:
#                 return render(request, 'signup.html', {
#                     'form': UserCreationForm,
#                     'error': 'Username already exists'
#                 })
#                 # return HttpResponse('Username already exists')
#         return render(request, 'signup.html', {
#             'form': UserCreationForm,
#             'error': 'Password do not match'
#         })




def mi_vista(request):
    path_hosts_switches = 'proyectnornir/inventory/switches.yaml'
    list_selecction = []

    if request.method == 'POST':
        switch1 = request.POST.get('switch1')
        switch2 = request.POST.get('switch2')  

        list_selecction.append(switch1)
        list_selecction.append(switch2)

        print(switch1)   
        print(switch2)

        create_hosts_yaml(list_selecction, path_hosts_switches)
        serialize_results_to_json()

        # return render(request, 'resultado.html', {'switch1': switch1, 'switch2': switch2})
        return redirect('download')
    return render(request, 'index.html')


def download(request):
    return render(request, 'download.html')


def HomePage(request):
    return render (request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        admin = request.POST.get('administrador')
        consultor = request.POST.get('consultor')
        print(admin, consultor)

        if pass1 != pass2:
            return HttpResponse('Your password do not the same')

        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        # return HttpResponse('User has been create successfully!!!')
        return redirect('login')
        # print(uname, email, pass1, pass2)

    return render (request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username = username, password = pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect!!!')

    return render (request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')