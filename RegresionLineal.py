#Predecir Salario en base a los años de experiencia

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head())

y = df['Salario'].values.reshape(-1,1)#Dependiente
X = df['Experiencia'].values.reshape(-1,1)#Independiente

#Usamos el 80% para entrenar y el 20% para evaluar de manera aleatoria
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
regresion_lineal = LinearRegression()
regresion_lineal.fit(X_train, y_train)

#indica que por cada año de experiencia, el salario subira en cierto monto
print('Coeficiente de regresión: ', regresion_lineal.coef_)
#El nivel de correlacion debe ser cercano a 1
print('Puntaje de regresión: ',regresion_lineal.score(X_test, y_test))