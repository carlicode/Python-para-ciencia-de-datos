#Extraer filas donde el CO2 sea mayor a 204

import numpy as np

emisiones = np.array(
[[2,4,13.7,9.4,382],
[4.3,4,14.3,9,347],
[4,4,9.5,8.5,327],
[4.4,6,18.4,7.1,377],
[2.7,6,13.7,9.3,294],
[3.1,6,19.4,6.4,297],
[4,4,9.6,13.3,313],
[1.8,6,11.5,18,207],
[6.3,4,11.6,9.6,253],
[5,6,11.3,9.7,269],
[2.8,8,13.1,10,235],
[2.2,8,13.2,10.6,235],
[2.8,8,13.3,6.9,307],
[4,8,11.9,6.7,354],
[4,8,12.9,5.7,337],
[3.9,8,12.6,5.8,368],
[3.8,6,13.1,6.1,327],
[4,6,12.8,5.9,205],
[5,6,13.3,6.5,193],
[6.7,6,19.7,6.1,207],
[4,6,16.7,5.9,209],
[2.9,8,19.7,8.4,200],
[2.7,8,16.7,8.3,193],
[3.1,4,10,9.6,235],
[3.6,4,11.5,10.2,239],
[3.9,4,9.3,11.2,230],
[2.1,4,12.2,7.2,278]])

#Filas con CO2 superior a 204
#:,4 significa que extraemos todas las columnas con el indice 4
filas_co2_alto = emisiones[emisiones[:, 4] > 204.0]
print(filas_co2_alto)