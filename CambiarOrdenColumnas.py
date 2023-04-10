#Intercambiar la columna ciudad por consumo autopista

import pandas as pd

df = pd.read_csv('emisiones_2_10.csv', delimiter=';')

#Intercambio el orden por el index de las columnas
df = df.iloc[:,[0,1,3,2,4]]

print(df)