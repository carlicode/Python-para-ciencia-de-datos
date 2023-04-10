#Es un algoritmo de aprendizaje no supervizado
#Cada punto se desplaza a la media regional
#La ubicacion de destino final de cada punto, representa el grupo al que pertence
#Es un algoritmo computacionalmente costoso

#Encontrar los clusters y graficarlos en 3D

from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs  
from matplotlib import pyplot as plt 

#Usar los datos generados para entrenar el modelo mean shift 
#Generamos nuestros propios datos
clusters = [[6,6,6], [2,2,2]]
X, y = make_blobs(centers = clusters, cluster_std = 0.70)

#E lalgoritmo mira y decide a donde moverse para determinar la ruta mas probable
#Las muestars generadas son X
bandwidth = estimate_bandwidth(X, n_samples=500)
meanshift = MeanShift(bandwidth=bandwidth)
meanshift.fit(X)
#Almacenamos los centros de los clusters
cluster_centers = meanshift.cluster_centers_


fig = plt.figure()
#Trazamos los datos y centroides en 3D
ax = fig.add_subplot(111, projection ='3d')

ax.scatter(X[:, 0], X[:, 1], marker ='.', color ="yellowgreen")
ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker ='o', color ='red', s=10, linewidth=5,  
            zorder=10)
plt.show()