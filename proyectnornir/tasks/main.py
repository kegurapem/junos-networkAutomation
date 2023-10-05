import json
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

from nornir import InitNornir
from nornir_netmiko import netmiko_send_config


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


# def create_user(name_user, password_user):
#     # Inicializa Nornir
#     nr = InitNornir(config_file="/home/kevin/junos-networkAutomation/proyectnornir/config.yaml")

#     # Comandos para crear el usuario y configurar el dispositivo
#     commands = [
#         f"set system login user {name_user} uid 2020 class super-user",
#         f'set system login user {name_user} full-name "usuario administrador"',
#         f"set system login user {name_user} authentication plain-text-password-value {password_user}",
#         "commit",
#     ]

#     # Ejecuta la tarea en el dispositivo
#     result = nr.run(task=netmiko_send_config, config_commands=commands)

#     # Puedes verificar la salida si lo deseas
#     print(result)


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

