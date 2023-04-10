import pandas as pd

df = pd.read_csv('empleados_2_2.csv', delimiter=';')

print(df.mean(axis=0))