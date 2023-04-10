#Estandarizacion de datos para poner en una misma escala de 0 a 1
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('datos.csv', delimiter=';')

#metodo para la normalizacion
scaler = MinMaxScaler()

#Nos devuelve un nuevo arreglo con los valores
scaled_df = scaler.fit_transform(df)

scaled_df = pd.DataFrame(scaled_df, columns=['Altura', 'Peso'])

print(scaled_df)
