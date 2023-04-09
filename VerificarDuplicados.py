import pandas as pd

#Leemos el archivo con pandas
df = pd.read_csv('empleados.csv', delimiter=';')

#Verifico duplicados
duplicates_rows = df[df.duplicated()]

#Visaulizo los datos duplicados en un nuevo dataframe
print(duplicates_rows)