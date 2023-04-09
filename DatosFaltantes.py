import pandas as pd

#Leemos el archivo con pandas
df = pd.read_csv('empleados.csv', delimiter=';')

#Averiguamos el tamaño del archivo CSV
print(df.shape)

#Imprimimos los valores nulos por cada columna
NaN = df.isnull().sum()
print(NaN)

#Imprimimos los NO valores nulos
NNaN = df.notnull().sum()
print(NNaN)