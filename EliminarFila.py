import pandas as pd

#Leemos el archivo con pandas
df = pd.read_csv('empleados.csv', delimiter=';')

#Especifico la columna que quiero eliminar que tiene puros valores nulos
df_column_no_null = df.drop(axis=1,columns=['Apellido'])

#Elimino las filas que tienen al menos un valor nulo
#Con Axis 0 estamos especificando las filas
df_row_no_null = df_column_no_null.dropna(axis=0)

#Eliminar filas que tengan al menos 5 valores No Nulos
df_row_no_null_5 = df_column_no_null.dropna(axis=0, thresh=5)
print(df_row_no_null_5)