#pip install faker
#pip install faker_food

from faker import Faker
from faker_food import FoodProvider
import pandas as pd

fake=Faker('es_Es')

fake.add_provider(FoodProvider)
Faker.seed(0)
farm=[]
verduras=['tomates','lechugas','zanahorias','pimientos','cebollas','patatas','calabacines','berenjenas','pepinos','calabazas','espárragos','judías','guisantes','habas','alcachofas']

tamaños=['grande','mediana','pequeña']
fertilizantes=['si','no']
v={}
v['tipo_cultivo']='d'
v['ubicacion_geografica']='d'
v['tamano_finca']='continuous'
v['rendimiento_cultivo']='continuous'
v['uso_fertilizantes']='d'
v['precio_venta(€/kg)']='d'
farm.append(v)
v={}
v['tipo_cultivo']=''
v['ubicacion_geografica']=''
v['tamano_finca']=''
v['rendimiento_cultivo']=''
v['uso_fertilizantes']=''
v['precio_venta(€/kg)']='class'
farm.append(v)

for i in range(5000):
    v={}
    v['tipo_cultivo']='Tomates'
    v['ubicacion_geografica']=fake.city()
    v['tamano_finca']=fake.random_int(min=1,max=100)
    v['rendimiento_cultivo']=fake.random_int(min=1,max=100)
    v['uso_fertilizantes']=fake.random_element(fertilizantes)
    v['precio_venta(€/kg)']=fake.random_int(min=1,max=100)
    farm.append(v)
df_farm = pd.DataFrame(farm)
df_farm.to_csv('agriculture_data.tab', header=True, index=False, sep="\t")

farm=[]
v={}
v['tipo_cultivo']='d'
v['ubicacion_geografica']='d'
v['tamano_finca']='continuous'
v['rendimiento_cultivo']='continuous'
v['uso_fertilizantes']='d'
v['precio_venta(€/kg)']='d'
farm.append(v)
v={}
v['tipo_cultivo']=''
v['ubicacion_geografica']=''
v['tamano_finca']=''
v['rendimiento_cultivo']=''
v['uso_fertilizantes']=''
v['precio_venta(€/kg)']='class'
farm.append(v)

for i in range(1250):
    v={}
    v['tipo_cultivo']='Tomates'
    v['ubicacion_geografica']=fake.city()
    v['tamano_finca']=fake.random_int(min=1,max=100)
    v['rendimiento_cultivo']=fake.random_int(min=1,max=100)
    v['uso_fertilizantes']=fake.random_element(fertilizantes)
    v['precio_venta(€/kg)']=fake.random_int(min=1,max=100)
    farm.append(v)
df_farm = pd.DataFrame(farm)
df_farm.to_csv('agriculture_datatest.tab', header=True, index=False, sep="\t")