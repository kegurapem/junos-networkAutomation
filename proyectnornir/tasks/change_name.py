from nornir import InitNornir
from nornir_netmiko import netmiko_send_config

def change_hostname(task, new_hostname):
    # Comandos para cambiar el nombre del dispositivo
    commands = [
        f"set system host-name {new_hostname}",
        "commit",
    ]

    # Envía los comandos al dispositivo utilizando Netmiko
    result = task.run(task=netmiko_send_config, config_commands=commands)

    # Puedes verificar la salida si lo deseas
    print(result[0].result)

# Inicializa Nornir
nr = InitNornir(config_file="/home/kevin/junos-networkAutomation/proyectnornir/config.yaml")

# Nombre nuevo que deseas configurar
new_hostname = "nuevo_nombre_switch"

# Ejecuta la tarea en el dispositivo
result = nr.run(task=change_hostname, new_hostname=new_hostname)
