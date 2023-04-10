#Determinar que clientes son similares
#Cuantos clientes pertenecen a un grupo
#Cuantos grupos existen

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import normalize
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv('clientes.csv', delimiter=";")

#Grafico el dendograma para decidir el num de grupos 
#Primero debo ver el dendograma y ver en 15000 cuantos grupos se formaron
#Despues de ver el grafico, verifico que son 3 grupos
dendrogram(linkage(df, method='ward',  metric='euclidean'))
plt.axhline(y=15000, color='r', linestyle='--')
plt.show()

#Digo que son 3 clusters
agglomerative = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
agglomerative.fit(df)

#Obtengo las etiquetas de los clusters
labels = agglomerative.labels_

print(labels)

#Visualizo los 3 grupos
plt.scatter(df['Salario'], df['Gasto'], c=labels) 
plt.xlabel('Salario Mensual')
plt.ylabel('Porcentaje Gasto Mensual')

plt.show()