import csv
from faker import Faker

fake = Faker('es_ES')

fields = ['Tipo de cultivo', 'Ubicación geográfica', 'Tamaño de la finca', 'Rendimiento del cultivo', 'Uso de fertilizantes', 'Precio de venta (euros el kilo)']
header = ['tipo_cultivo', 'ubicacion_geografica', 'tamano_finca', 'rendimiento_cultivo', 'uso_fertilizantes', 'precio_venta (€/kg)']

with open('agriculture_data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()

with open('agriculture_data.csv', mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    for i in range(6000):
        row = {
            'tipo_cultivo': 'Tomates',
            'ubicacion_geografica': fake.address(),
            'tamano_finca': fake.random_int(min=1, max=100),
            'rendimiento_cultivo': fake.random_int(min=100, max=1000),
            'uso_fertilizantes': fake.random_element(elements=('Sí', 'No')),
            'precio_venta (€/kg)': fake.random_int(min=1, max=8)
        }
        writer.writerow(row)
