import yaml

# Obtener datos de los host del archivo original
def get_ips(path_nornir_switches):
    # Lista para almacenar los datos de los host
    ip_switch = []

    with open(path_nornir_switches, "r") as file:
        switches_data = list(yaml.safe_load_all(file))

    for item in switches_data:
        for valor in item.values():
            ip_switch.append(valor['hostname'])
    
    return ip_switch

# print(get_ips("prueba/switches.yaml"))

print('----------------------------------------------------------------------------------------------')

# ip_switches = get_ips("prueba/switches.yaml")

# Iterar sobre los datos recibidos y crear el archivo new.yaml con separadores y formato correcto

def create_hosts_yaml(list_selecction, path_hosts_switches):
    # obtener datos de todos los switches registrados en else
    with open(path_hosts_switches, "r") as file:
        switches_data = list(yaml.safe_load_all(file))
        # print(f'switches_data: {switches_data}')

    ip_switches = get_ips(path_hosts_switches)
    # print(f'ip_switches: {ip_switches}')

    # with open('prueba/new.yaml', 'w') as archivo:
    with open('/home/kevin/junos-networkAutomation/proyectnornir/inventory/hosts.yaml', 'w') as archivo:
        archivo.write("---")
        for element in list_selecction:
            # print(f'element: {element}')
            if element in ip_switches:
                for data in switches_data:
                    # print(data)
                    for key, value in data.items():
                        if value['hostname'] == element:
                            archivo.write("\n")
                            yaml.dump({key: value}, archivo, default_flow_style=False)
    
    return print('creación exitosa del archivo hosts.yaml')


list_selecction = ['10.1.8.131', '10.1.8.132', '10.1.8.133']
path_hosts_switches = 'prueba/switches.yaml'
# path_hosts_switches= 
create_hosts_yaml(list_selecction, path_hosts_switches)