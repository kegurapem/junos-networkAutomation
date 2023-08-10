import yaml

with open("prueba/switches.yaml", "r") as file:
    switches_data = list(yaml.safe_load_all(file))

# Lista para almacenar los datos de los host
ip_switch = []
data_recibida = ['10.1.8.131', '10.1.8.132']

# Iterar sobre la lista original y extraer los datos de los host
for item in switches_data:
    for valor in item.values():
        ip_switch.append(valor['hostname'])

# Imprimir la nueva lista con los datos de los host
print(ip_switch)


for element in data_recibida:
    print(f'element: {element}')
    contador = 0
    if element in ip_switch:
        print(ip_switch)
        with open('prueba/new.yaml', 'w') as archivo:
            yaml.dump(switches_data[contador], archivo, default_flow_style=False)
            # print(switches_data[1])
    else:
        print('pipipipi')
    
    contador = contador + 1

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


