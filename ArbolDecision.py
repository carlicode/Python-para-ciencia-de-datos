#Cada nodo se divide en 2 hojas
#Cada una de las hojas pueden ser nodos de decision

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

#Crea datos con x y y que forman semi lunas para problemas de agrupación
X, y = make_moons(n_samples=5000, noise=0.3, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

arbol_decision = DecisionTreeClassifier()
arbol_decision.fit(X_train, y_train)

precision = arbol_decision.score(X_test, y_test)
print('La precisión es ', precision*100)