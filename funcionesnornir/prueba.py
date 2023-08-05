import yaml

# Definir la condición para determinar si se debe cargar/copiar/integrar la información
test = True

if test:
    data_to_insert = {
        "switch.access-01": {
            "hostname": "10.1.8.131",
            "groups": ["junos_group_cusco"],
            "data": {
                "layer": "layer 2"
            }
        }
    }

    # Leer el contenido actual del archivo ejemplo.yaml (si existe)
    try:
        with open("ejemplo.yaml", "r") as file:
            existing_data = yaml.safe_load(file)
    except FileNotFoundError:
        existing_data = {}

    # Integrar o reemplazar la información en el archivo
    existing_data.update(data_to_insert)

    # Guardar la información actualizada en el archivo ejemplo.yaml
    with open("/home/kevin/junos-networkAutomation/myapp/pruebas/ejemplo.yaml", "w") as file:
        yaml.dump(existing_data, file)
