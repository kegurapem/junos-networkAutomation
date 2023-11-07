from django.shortcuts import render, redirect
from proyectnornir.tasks.main import serialize_results_to_json, create_user  # Importa la función saludo desde saludo.py
from funcionesnornir.create_hosts import create_hosts_yaml
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
import os
import json
from .models import UsuarioNornir
from django.http.response import JsonResponse


def mi_vista(request):
    path_hosts_switches = 'proyectnornir/inventory/switches.yaml'
    list_selecction = []

    if request.method == 'POST':
        switch1 = request.POST.get('switch1')
        switch2 = request.POST.get('switch2')  

        list_selecction.append(switch1)
        list_selecction.append(switch2)

        getconfig = request.POST.get('getconfig')

        print(switch1)   
        print(switch2)

        create_hosts_yaml(list_selecction, path_hosts_switches)

        if getconfig == 'get_facts':
            serialize_results_to_json()
        else:
            pass

        # return render(request, 'resultado.html', {'switch1': switch1, 'switch2': switch2})
        return redirect('download')
    return render(request, 'index.html')
    # return render(request, 'download.html')


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
        print(uname, email,pass1)

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

    return render (request, 'login_nornir.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')



def descargar_json(request):
    ruta = "/home/kevin/junos-networkAutomation/proyectnornir/"
    nombre_archivo = "result.json"
    existe_json(ruta, nombre_archivo)

    if request.method == 'POST':
        print('estoy haciendo un post')
        # Ruta al archivo JSON que deseas descargar
        json_file_path = '/home/kevin/junos-networkAutomation/proyectnornir/result.json'

        # Verificar si el archivo existe
        if os.path.exists(json_file_path):
            with open(json_file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/json')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(json_file_path)}"'
                return response
        else:
            return HttpResponse('El archivo no se encontró', status=404)

        # return render(request, 'resultado.html', {'switch1': switch1, 'switch2': switch2})
        # return redirect('download')
    else:
        json_file_path = '/home/kevin/junos-networkAutomation/proyectnornir/result.json' 
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as file:
                json_content = json.load(file)  # Cargar el contenido JSON
                print(json_content)
            return render(request, 'download.html', {'json_content': json_content})
        else:
            # return HttpResponse('El archivo no se encontró', status=404)
            return render(request, 'download.html')
    # return render(request, 'download.html')



def existe_json(ruta, nombre_archivo):

    # Ruta completa del archivo JSON
    ruta_completa = os.path.join(ruta, nombre_archivo)

    # Verificar si el archivo JSON existe
    if os.path.exists(ruta_completa):
        print(f"El archivo {nombre_archivo} existe en la ruta especificada.")
    else:
        print(f"El archivo {nombre_archivo} no existe en la ruta especificada.")


def usuarios_nornir(request):
    return render(request, 'usuarios_nornir.html')


def list_usuarios_norrnir(request):
    usersnornir = list(UsuarioNornir.objects.values())
    data = {'usuarios_nornir': usersnornir}
    return JsonResponse(data)

# ---- A partir de aquí correo el código funcional ordenado ----

# def HomePage(request):
#     return render(request, 'home1.html')


# def HomePage(request):
#     my_user = request.user  # Obtiene al usuario actual
#     return render(request, 'home1.html', {'my_user': my_user})

def HomePage(request):
    my_user = request.user  # Asegúrate de que user esté disponible en el contexto.
    template_name = 'layouts/base-admin.html' if my_user.is_authenticated and my_user.is_staff else 'layouts/base-consultor.html'
    return render(request, 'home1.html', {'my_user': my_user, 'template_name': template_name})


def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname1 = request.POST.get('lastname1')
        lastname2 = request.POST.get('lastname2')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        permiso = request.POST.get('permiso')

        if password1 != password2:
            return HttpResponse("Your password and confrom password are not same")

        print(permiso)
        if permiso == 'admin':
            my_user = User.objects.create_superuser(name, lastname1, password1)
            my_user.save()
        else:
            my_user = User.objects.create_user(name, lastname1, password1)
            my_user.save()

        return redirect('login1')

    return render(request, 'signup1.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('home1')
        else:
            return HttpResponse('Username or Password is incorrect!')

    return render(request, 'login1.html')


def LogoutPage(request):
    logout(request)
    return redirect('login1')


# Funciones para listar usuarios en la interfaz usuarios_nornir.html - en la ruta http://127.0.0.1:8000/usersnornir2/
def users_nornir(request):
    return render(request, 'users_nornir.html')


def list_users_nornir(request):
    usersnornir = list(User.objects.values())
    data = {'usuarios_nornir': usersnornir}
    return JsonResponse(data)


def config(request):
    path_hosts_switches = 'proyectnornir/inventory/switches.yaml'
    list_selecction = []

    if request.method == 'POST':
        switch1 = request.POST.get('switch1')
        switch2 = request.POST.get('switch2') 

        name_user = request.POST.get('username')
        password_user = request.POST.get('password')

        permiso = request.POST.get('permiso')

        list_selecction.append(switch1)
        list_selecction.append(switch2)

        print(switch1, switch2, name_user, password_user, permiso)   

        create_hosts_yaml(list_selecction, path_hosts_switches)

        # Crear usuario en el switch
        create_user(name_user, password_user, permiso)

        # Crear usuario en la BD
        print(permiso)
        if permiso == 'admin':
            my_user = User.objects.create_superuser(name_user, "", password_user)
            my_user.save()
        else:
            my_user = User.objects.create_user(name_user, "", password_user)
            my_user.save()

        # return render(request, 'resultado.html', {'switch1': switch1, 'switch2': switch2})
        return redirect('usersnornir2')
    return render(request, 'config.html')
