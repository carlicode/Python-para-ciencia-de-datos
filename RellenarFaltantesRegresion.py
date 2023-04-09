import pandas as pd
from sklearn.linear_model import LinearRegression

#Leemos el archivo con pandas
df = pd.read_csv('empleados_7.csv', delimiter=';')

#Creo la regresion lineal
lineal_regression_model = LinearRegression()

#Vemos cuántos valores nulos tenemos por columna
print(df.isnull().sum())

#Dataframe con los datos nulos
null_data = df[df['Edad'].isnull()==True]

#Dataframe con los datos NO NULOS que serviran para el entrenamiento
train_data = df[df['Edad'].isnull()==False]

#Variables de entrada y de salida para la regresion lineal
y_train = train_data['Edad'] #Datos de edad
x_train = train_data.drop('Edad', axis=1) #Todos datos menos la edad

#Entrenamos modelo
lineal_regression_model.fit(x_train,y_train)

#Eliminamos la columna de edad para tener los valores para de entrada para realizar la prediccion
predict_data = null_data.drop('Edad', axis=1)

#Predecimos
predictions =  lineal_regression_model.predict(predict_data)
#print(predictions)

#Obtengo los nuevos valores en un nuevo dataframe
predict_data['Edad'] = predictions
print(predict_data)


