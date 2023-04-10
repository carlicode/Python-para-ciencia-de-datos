#

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Latitud y Longitud de lugares en Costa Rica
df = pd.read_csv('clusters.csv', delimiter=";")

#Divido los grupos en 4
kmeans = KMeans(n_clusters=4)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)

#Guardo en un array los centroides de cada grupo
cluster_centers = kmeans.cluster_centers_

#Grafico 
plt.scatter(df['Latitud'], df['Longitud'], c=y_kmeans, s=20)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200)
plt.xlabel('Latitud')
plt.ylabel('Longitud')

plt.show()