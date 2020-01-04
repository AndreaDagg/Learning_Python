"""
REGRESSIONE LINEARE
FUNZIONE DI COSTO

Per torvare il valore ottimo devo ottimizzare il Gradietn Descent
"""
import pandas as pd
import numpy as np

boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", sep='\s+',
                     usecols=[5, 13], names=["RM", "MEDV"])
print(boston.head())
X = boston.drop("MEDV", axis=1).values
Y = boston["MEDV"].values

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

"""
Costruiamo il modello predittivo
"""
from sklearn.linear_model import LinearRegression

ll = LinearRegression()
ll.fit(X_train, Y_train)  # costruisce il modello il metodo fit
Y_pred = ll.predict(X_test)  # il metodo predict effettua la predizione

"""
Ora dobbiamo valutare la funzione di costo tramite l'errore quadratico medio che però non ci da una misura oggettiva per farlo dobbiamo utilizzare
coefficiente di determinazione che standardizza L'MSE (non è di costo ma di punteggio quidni piú tende ad 1 migliore è)

Per valori > 0.3 il modello è inutile, tra 0,3 e 0,5 e scarso, 0,5 e 0,7 è discreto, tra 0,7 e 0,9 è ottimo se è == 1 c'è un errore

"""
from sklearn.metrics import mean_squared_error

print(mean_squared_error(Y_test, Y_pred))

from sklearn.metrics import r2_score

print(r2_score(Y_test, Y_pred))

# Costruiamo il grafico
import matplotlib.pyplot as plt

print("Peso di RM: " + str(ll.coef_[0]))
print("Bias: " + str(ll.intercept_))

plt.scatter(X_train, Y_train, c="green", edgecolors="white")
plt.scatter(X_test, Y_test, c="blue", edgecolors="white")
plt.xlabel("Numero Medio di stanze [RM]")
plt.ylabel("Valore in $ [MEDV]")
plt.plot(X_test,Y_pred)
plt.show()