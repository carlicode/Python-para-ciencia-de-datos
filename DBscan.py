#Calcula graficos de vecinos mas vecinos


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN


df = pd.read_csv('datos.csv', delimiter=";")
print(df.head())

#Creo objeto dbscan
dbscan = DBSCAN()
dbscan.fit(df)
#obtengo las etiquetas
labels = dbscan.labels_

print(labels)

plt.scatter(df['Variable1'],df['Variable2'], c=labels, cmap= "plasma")
plt.show()