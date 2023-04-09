import pandas as pd

#Leemos el archivo con pandas
df = pd.read_csv('empleados.csv', delimiter=';')

#Eliminar duplicados
duplicates_deleted = df.drop_duplicates()

#Visaulizo el df con los duplicados eliminados 
print(duplicates_deleted)