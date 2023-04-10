#Identifica valores atipicos, pued eencontrar compras fraudulentas dado un patron de compra
#Detectar salarios atipicos con IsolationForest
#1 es normal -1 es anormal

import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv('empleados_3_7.csv', delimiter=";")

isolation_forest = IsolationForest(random_state=42)
#Entrenamos el modelo con el salario
isolation_forest.fit(df[['Salario']])

#La columna normal me devuelve los valores atipicos y normales
df['Normal'] = isolation_forest.predict(df[['Salario']])

print(df[['Salario', 'Normal']])

print(df['Normal'].value_counts())