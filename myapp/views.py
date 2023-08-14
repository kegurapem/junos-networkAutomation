from django.shortcuts import render, redirect
from proyectnornir.tasks.main import serialize_results_to_json  # Importa la función saludo desde saludo.py
from funcionesnornir.create_hosts import create_hosts_yaml
from django.http import HttpResponse
import os


# Create your views here.
# def index(request):
#     return render(request, 'index.html', {
#         'hello': hello()
#     })
# ***********************************************************************************

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