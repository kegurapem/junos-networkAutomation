# import yaml

# with open("prueba/switches.yaml", "r") as file:
#     switches = list(yaml.safe_load_all(file))

# # Lista todos los documentos YAML en el archivo
# # print(switches)

# # Accede a un documento YAML específico
# # print("Switch 1:")
# # print(switches[0])  # Accede al primer documento
# # print("---")

# switch1 = False
# switch2 = False

# if switch1 == True:
#     print(switches[0])
# elif switch2 == True:
#     print(switches[1])
# else:
#     print('pipipip')

import yaml

data1 = ['switch.access-01', 'switch.access-02']

with open("prueba/switches.yaml", "r") as file:
    switches_data = list(yaml.safe_load_all(file))


print(switches_data)
# print(switches_data[0])
# Ahora switches_data es una lista con cada switch representado como un diccionario
# Puedes realizar operaciones sobre los switches en el bucle
# lista_switches = list(switches_data.keys())[0]
# print(lista_switches)
# for switch_data in switches_data:
#     # switch_name = list(switch_data.keys())[0]  # Obtén el nombre del switch del diccionario
#     # print(f"Información del switch '{switch_name}':")
#     # print(switch_data[switch_name])
#     # print("---")
    
#     if data1[0] == list(switch_data.keys())[0]:
#         print(list(switch_data.keys())[0])
#         # Información del switch "switch.access-01"
#         # new_switch_data = switches_data[0]

#         # # Guardar la información en el archivo "ejemplo.yaml"
#         # with open("/home/kevin/junos-networkAutomation/prueba/ejemplo.yaml", "w") as file:
#         #     yaml.dump(new_switch_data, file)


