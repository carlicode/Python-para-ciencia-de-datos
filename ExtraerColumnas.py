#Extraer columnas que sean tipo numerico 

import pandas as pd

df = pd.read_csv('emisiones.csv', delimiter=';')

#Imprimo la info de tipos de datos de las columnas
print(df.info())

#Seleccionamos las columnas numericas 
numeric_columns = df.select_dtypes(include=['float', 'int'])

print(numeric_columns)