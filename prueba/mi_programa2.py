import yaml

with open("prueba/switches.yaml", "r") as file:
    switches_data = list(yaml.safe_load_all(file))

# Lista para almacenar los datos de los host
ip_switch = []

# Obtener datos de los host del archivo original
for item in switches_data:
    for valor in item.values():
        ip_switch.append(valor['hostname'])

data_recibida = ['10.1.8.131', '10.1.8.132']

# Iterar sobre los datos recibidos y crear el archivo new.yaml
for element in data_recibida:
    print(f'element: {element}')
    if element in ip_switch:
        for data in switches_data:
            for key, value in data.items():
                if value['hostname'] == element:
                    with open('prueba/new.yaml', 'a') as archivo:
                        yaml.dump({key: value}, archivo, default_flow_style=False)
    else:
        print('pipipipi')
