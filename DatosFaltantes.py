import pandas as pd

#Leemos el archivo con pandas
file = pd.read_csv('empleados.csv', delimiter=';')

#Averiguamos el tamaño del archivo CSV
print(file.shape)

#Imprimimos los valores nulos por cada columna
NaN = file.isnull().sum()
print(NaN)

#Imprimimos los NO valores nulos
NNaN = file.notnull().sum()
print(NNaN)