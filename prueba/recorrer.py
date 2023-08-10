import yaml


# Ruta al archivo YAML
ruta_archivo = '/home/kevin/junos-networkAutomation/prueba/switches.yaml'
# Cargar el contenido completo del archivo YAML en una variable
with open(ruta_archivo, 'r') as archivo:
    switchesyaml = archivo.read()

# Carga el contenido YAML
contenidoyaml = yaml.safe_load_all(switchesyaml)

listipswitches = []
# Recorre el contenido del archivo YAML
for data in contenidoyaml:
    detalles = next(iter(data.values()))  # Obtiene los detalles del switch
    print(detalles)
    hostname = detalles['hostname']
    listipswitches = listipswitches + [hostname]

# output de todo el codigo de arriba
# listipswitches = ['10.1.8.131', '10.1.8.132']

# data a recibir
ips = ['10.1.8.133', '10.1.8.132']

contador = 0

for elemento in listipswitches:
    if elemento in ips:
        contador = contador + 1

print(f'existes {contador} respetidos')
