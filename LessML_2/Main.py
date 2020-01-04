import pandas as pd
import numpy as np

shirts = pd.read_csv("data/shirts.csv", index_col=0)
print(shirts.head())

# Creaiamo un array numpy contente il dataset
X = shirts.values
print(X[:10])

# Rielaboriamo i char (ordinabili) in numeri definendo un dizionario
size_mapping = {"S": 0, "M": 1, "L": 2, "XL": 3}

shirts["taglia"] = shirts["taglia"].map(size_mapping)
print(" - CAMBIO VALORE - ")
print(shirts.head())

# utyilizzare numpy
fmap = np.vectorize(lambda t: size_mapping[t])
X[:, 0] = fmap(X[:, 0])

# Per Rielaborare stringhe non ordinabili logicamente applichiamo Why not encoding
shirts = pd.get_dummies(shirts, columns=["colore"])
print(" - Applicare Why not encoder - ")
print(shirts.head())

# utilizzare numpy
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# le = LabelEncoder()
# enc = OneHotEncoder(categories=[1])
# X[:, 1] = le.fit_transform(X[:, 1])
# X_sparse = enc.fit_transform(X)
# X = X_sparse.toarray()


"""
Lavorare con dataset a cui mancano dati che hanno NaN 

"""
iris_nan = pd.read_csv("data/iris_nan.csv")
Y = iris_nan["class"].values
X = iris_nan.drop("class", axis=1).values
print(iris_nan)

# 1 Metodo rimuyovere le righe o colkonne con valori mancanti
iris_drop = iris_nan.dropna()  # elimina la riga con Nan
iris_drop = iris_nan.dropna(axis=1)  # elimina la colonna con NAN

# 2 Metodo imputazione dei valori mancati con altri ad esempio la media (mean), moda (mode().iloc[0])

replace_with = iris_nan.mean()  # calcolo la media
iris_imp = iris_nan.fillna(replace_with)  # la inserisco dove NaN

