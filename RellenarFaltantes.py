import pandas as pd

#Leemos el archivo con pandas
df = pd.read_csv('empleados_6.csv', delimiter=';')

#Llenamos los datos faltantes con la media
df['Edad'] = df['Edad'].fillna(df['Edad'].mean())

#Verifico el num de datos faltantes por columna
df_missed_values_filled = df.isnull().sum()

print(df_missed_values_filled)