import yaml

# with open('data.yaml', 'r') as file:
#     data = yaml.safe_load(file)

# print(data)
# keys = data.keys()
# print(keys)


# with open('switches.yaml', 'r') as file:
#     ejemplo = yaml.safe_load_all(file)

# print(ejemplo)


# with open('EXAMPLE.yaml', 'a') as file:
#     yaml.dump(ejemplo, file)
ipget = ['10.8.131', '10.1.8.132']

def read_yaml(data):
    with open(data, 'r') as file:
        # example = yaml.safe_load_all(file)
        example = list(yaml.safe_load_all(file))

    return example

# print(read_yaml('switches.yaml'))

switches = read_yaml('switches.yaml')
direccion_ip = switches[0]['switch.access-01']['hostname']
print(direccion_ip)






# switches = read_yaml('switches.yaml')

def check_ips(ipget):
    switches = read_yaml('switches.yaml')
    direccion_ip = switches[0]['switch.access-01']['hostname']
    for ip in ipget:
        if ip in direccion_ip:
            print(direccion_ip)
    # return

check_ips(ipget)