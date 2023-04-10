#Agregar fila con datos nuevos
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('temperaturas.csv', delimiter=';')

new_temp = pd.DataFrame.from_dict([{'Año' : '2022', 'temperatura': '74.3'}])

#Agregamos nuevo dataFrame 
df = pd.concat([df, new_temp], ignore_index=True)

print(df)