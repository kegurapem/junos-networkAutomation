from django.shortcuts import render, redirect
from proyectnornir.tasks.main import serialize_results_to_json  # Importa la función saludo desde saludo.py
from funcionesnornir.create_hosts import create_hosts_yaml
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login

# Create your views here.
# def index(request):
#     return render(request, 'index.html', {
#         'hello': hello()
#     })
# ***********************************************************************************

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return HttpResponse('User created successfully')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
                # return HttpResponse('Username already exists')
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })




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



# list_selecction = ['10.1.8.131', '10.1.8.132', '10.1.8.133']
# path_hosts_switches = 'proyectnornir/inventory/switches.yaml'
# # path_hosts_switches= 
# create_hosts_yaml(list_selecction, path_hosts_switches)