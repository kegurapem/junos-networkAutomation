# from nornir import InitNornir
# from nornir_netmiko import netmiko_send_config

# def configure_user(task, new_password):
#     # Comandos para configurar el usuario y establecer la contraseña
#     commands = [
#         "set system login user admin-kegura uid 2020 class super-user",
#         'set system login user admin-kegura full-name "usuario administrador"',
#         "set system login user admin-kegura authentication plain-text-password-value juniper123",
#         "commit",
#     ]

#     # Envía los comandos al dispositivo utilizando Netmiko
#     result = task.run(task=netmiko_send_config, config_commands=commands)

#     # Puedes verificar la salida si lo deseas
#     print(result[0].result)

# # Inicializa Nornir
# nr = InitNornir(config_file="/home/kevin/junos-networkAutomation/proyectnornir/config.yaml")

# # Ejecuta la tarea en el dispositivo
# result = nr.run(task=configure_user, new_password=new_password)


from nornir import InitNornir
from nornir_netmiko import netmiko_send_config

def create_user(task, name_user, password_user):
    # Comandos para cambiar el nombre del dispositivo
    commands = [
        f"set system login user {name_user} uid 2020 class super-user",
        f'set system login user {name_user} full-name "usuario administrador"',
        f"set system login user {name_user} authentication plain-text-password-value {password_user}",
        "commit",
    ]

    # Envía los comandos al dispositivo utilizando Netmiko
    result = task.run(task=netmiko_send_config, config_commands=commands)

    # Puedes verificar la salida si lo deseas
    print(result[0].result)

# Inicializa Nornir
nr = InitNornir(config_file="/home/kevin/junos-networkAutomation/proyectnornir/config.yaml")

# Nombre nuevo que deseas configurar
name_user = "admin-ulises"
password_user = "juniper123"

# Ejecuta la tarea en el dispositivo
result = nr.run(task=create_user, name_user=name_user, password_user=password_user)
