# from nornir import InitNornir
# from nornir_utils.plugins.functions import print_result
# from nornir_napalm.plugins.tasks import napalm_get
# import json

# nr = InitNornir(
#     # config_file="config.yaml", dry_run=True
#     config_file="config.yaml"
# )

# results = nr.run(
#     # task=napalm_get, getters=["facts", "interfaces"]
#     # task=napalm_get, getters=["config"]
#     task=napalm_get, getters=["get_facts"]
# )
# # print_result(results)
# print(results)
# # # Paso 1: Convertir el diccionario a formato JSON
# # data_json = json.dumps(results, indent=4)  # El parámetro 'indent' agrega indentación para hacerlo más legible

# # # Paso 2: Escribir los datos en el archivo "ejemplo.json"
# # with open('result.json', 'w') as archivo:
# #     archivo.write(data_json)


# ********************************************************************************
# import json
# from nornir import InitNornir
# from nornir_napalm.plugins.tasks import napalm_get

# nr = InitNornir(config_file="config.yaml")

# results = nr.run(task=napalm_get, getters=["get_facts"])

# # Paso 1: Extraer la información relevante para la serialización
# data_to_serialize = {}
# for hostname, result in results.items():
#     data_to_serialize[hostname] = result[0].result

# # Paso 2: Convertir los datos a formato JSON
# data_json = json.dumps(data_to_serialize, indent=4)

# # Paso 3: Escribir los datos en el archivo "result.json"
# with open('result.json', 'w') as archivo:
#     archivo.write(data_json)

# ********************************************************************************
import json
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

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

# Uso de la función
serialize_results_to_json()
