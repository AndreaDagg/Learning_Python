import pandas as pd

iris = pd.read_csv("data/iris.csv")

# visualizzare solo i primi / ultimi 10 elementi del csv
# Se non lo sono possiamo definire come priam riga il nopme delle colonne del file
print(iris.head(10))
print(iris.tail())

# Leggere una / piú colonna
Y = iris['species']
print(Y.head())

X = iris[["species", "sepal_length"]]
print(X.head())

print(iris.drop("species", axis=1).head())

iris.shape  # righe e colonne
iris.describe()  # analisi statistica
iris["sepal_length"].var()  # varianza su un singola

# Maschera calcolo valore medio
petalo_maggioredellamedia = iris["petal_length"] > iris["petal_length"].mean()
iris_long_petals = iris[petalo_maggioredellamedia]
print(iris_long_petals)

# SORT
print(iris.sort_values("petal_length").head)

import matplotlib.pyplot as plt

iris.plot(x='sepal_length', y='sepal_width', kind='scatter')
plt.show()
