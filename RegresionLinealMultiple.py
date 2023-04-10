#Predecir el monto de CO2 que un auto emitira segun su altura, anchura y longitud

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

df = pd.read_csv('emisiones.csv', delimiter=";")

#Dividimos los datos en 2 matrices
y = df[['CO2']]#Variable dependiente
X = df[['Longitud', 'Anchura', 'Altura']]#Variables independientes

#80% train 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

regresion_lineal = LinearRegression()

regresion_lineal.fit(X_train, y_train)
y_pred=regresion_lineal.predict(X_test)

#Diferencia en positivo entre el valor real y el aproximado
print("Error absoluto medio: ", metrics.mean_absolute_error(y_test, y_pred))
print("Error cuadrático medio: ", metrics.mean_squared_error(y_test, y_pred))
#LA raiz debe estar mas cercano a cero
print("Raíz del error cuadrático medio: ",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))