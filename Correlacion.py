import pandas as pd
import seaborn as sns

df = pd.read_csv('empleados_2_1.csv', delimiter=';')

#Obtenemos correlacion entre los años de experiencia y el salario que reciben
#Calcula el coeficiente de coorrelacion de Pearson
Pearson = df['Experiencia'].corr(df['Salario'])
print(Pearson)

#Imprimimos mapa de calor
print(sns.heatmap(df.corr(numeric_only=True),vmin= -1, vmax=1, annot=True))



