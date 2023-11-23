import json
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

from nornir import InitNornir
from nornir_netmiko import netmiko_send_config

from nornir_netmiko.tasks import netmiko_send_command
# import datetime
# from django.db.models import F
import os
import shutil
import zipfile




def serialize_results_to_json(config_file="/home/kevin/junos-networkAutomation/proyectnornir/config.yaml"):
    # Paso 1: Inicializar Nornir con el archivo de configuración
    nr = InitNornir(config_file=config_file)

    # Paso 2: Ejecutar la tarea para obtener los datos
    results = nr.run(task=napalm_get, getters=["get_facts"])

    print_result(results)

    # Paso 3: Extraer la información relevante para la serialización
    data_to_serialize = {}
    for hostname, result in results.items():
        data_to_serialize[hostname] = result[0].result

    # Paso 4: Convertir los datos a formato JSON
    data_json = json.dumps(data_to_serialize, indent=4)

    # Paso 5: Escribir los datos en el archivo "result.json"
    with open('/home/kevin/junos-networkAutomation/proyectnornir/result.json', 'w') as archivo:
        archivo.write(data_json)


def create_user(name_user, password_user, permiso):
    # Inicializa Nornir
    nr = InitNornir(config_file="/home/kevin/junos-networkAutomation/proyectnornir/config.yaml")

    if permiso == 'admin':
        # Comandos para crear el usuario y configurar el dispositivo
        commands = [
            f"set system login user {name_user} uid 2020 class super-user",
            f'set system login user {name_user} full-name "usuario administrador"',
            f"set system login user {name_user} authentication plain-text-password-value {password_user}",
            "commit",
        ]
    else:
        commands = [
            f"set system login user {name_user} uid 2020 class operator",
            f'set system login user {name_user} full-name "usuario operador"',
            f"set system login user {name_user} authentication plain-text-password-value {password_user}",
            "commit",
        ]

    # Ejecuta la tarea en el dispositivo
    result = nr.run(task=netmiko_send_config, config_commands=commands)

    # Puedes verificar la salida si lo deseas
    print(result)

def loadFactoryDefault(password_root, name_user, password_user, ip, netmask):
    # Inicializa Nornir
    nr = InitNornir(config_file="/home/kevin/junos-networkAutomation/proyectnornir/config.yaml")

    commands = [
        f"load factory-default",
        f"set system root-authentication plain-text-password-value {password_root}",
        f"set system login user {name_user} uid 2000 class super-user",
        f'set system login user {name_user} full-name "usuario administrador"',
        f"set system login user {name_user} authentication plain-text-password-value {password_user}",
        f"set system services ssh",
        f"set system services netconf ssh",
        f"set interfaces me0 unit 0 family inet address {ip}/{netmask}",
        "commit",
        ]

    # Ejecuta la tarea en el dispositivo
    result = nr.run(task=netmiko_send_config, config_commands=commands)

    # Puedes verificar la salida si lo deseas
    print(result)


def save_config_to_file(ip_list):
    # Directorio base
    base_directory = "/home/kevin/junos-networkAutomation/proyectnornir"
    backup_directory = os.path.join(base_directory, "backup")

    # Verificar si la carpeta de respaldo existe; si existe, elimínala
    if os.path.exists(backup_directory):
        shutil.rmtree(backup_directory)

    # Crea una carpeta de respaldo limpia
    os.makedirs(backup_directory)

    # Inicializa Nornir
    nr = InitNornir(config_file=os.path.join(base_directory, "config.yaml"))

    # Comando a ejecutar
    command = "show configuration | display set"

    for ip in ip_list:
        # Genera un nombre de archivo único basado en la dirección IP
        output_file = os.path.join(backup_directory, f"backup_{ip}.txt")

        # Filtra el host correspondiente a la dirección IP en la lista
        filtered_host = nr.filter(hostname=ip)  # Filtro directo por la dirección IP

        for __, result in filtered_host.run(task=netmiko_send_command, command_string=command).items():
            with open(output_file, "w") as file:
                file.write(result.result)


def create_backup_zip():
    # Directorio base donde se encuentra la carpeta "backup"
    base_directory = "/home/kevin/junos-networkAutomation/proyectnornir"

    # Nombre del archivo ZIP de respaldo
    backup_zip_file = "backup.zip"

    # Ruta a la carpeta de respaldo
    backup_directory = os.path.join(base_directory, "backup")

    # Crear un archivo ZIP que contiene la carpeta de respaldo y su contenido
    with zipfile.ZipFile(backup_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(backup_directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, backup_directory)
                zipf.write(file_path, arcname)

    return backup_zip_file


