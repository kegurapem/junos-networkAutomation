from nornir import InitNornir
from nornir_netmiko import netmiko_send_config
from nornir.core.task import Task, Result

# Inicializa Nornir con la configuración adecuada
nr = InitNornir(config_file="/home/kevin/junos-networkAutomation/proyectnornir/config.yaml")

# Define una función para crear un usuario en Junos
def create_user(task: Task, username: str, password: str):
    # Comandos para crear un usuario en Junos
    commands = [
        f"set system login user {username} uid 2000 class super-user",
        f'set system login user {username} full-name "usuario administrador"',
        f"set system login user {username} authentication plain-text-password",
        f"{password}",  # Aquí ingresamos la contraseña
        f"{password}",  # Aquí ingresamos la misma contraseña nuevamente
        "commit",
    ]

    # Ejecutar comandos de configuración a través de SSH utilizando Netmiko
    config_commands = "\n".join(commands)
    result = task.run(
        task=netmiko_send_config,
        config_commands=config_commands,
    )

    # Verificar si la tarea fue exitosa
    if "Error" in result.result:
        return Result(
            host=task.host,
            failed=True,
            result=result.result,
            changed=False,
        )
    else:
        return Result(
            host=task.host,
            changed=True,
        )

# Llama a la función para crear el usuario en cada dispositivo Junos
result = nr.run(
    task=create_user,
    username="admin-else2",  # Nombre de usuario
    password="tu_contraseña",  # Contraseña deseada
)

# Imprime los resultados
for host, task_result in result.items():
    if task_result.failed:
        print(f"Error en el dispositivo {host}: {task_result.result}")
    else:
        print(f"Usuario creado en el dispositivo {host}")
