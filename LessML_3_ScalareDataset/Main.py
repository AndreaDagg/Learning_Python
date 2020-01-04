"""
Bisogna portare il dataset sulla stessa scala perché se i valori dei dati sono sufficentemente differenti l'algoritmo
potrebbe dare piú importanza ai valori piú grandi non essendo piú sufficientemente preciso.
I modelli come gli alberi decisionali non soffrono di questo problema.

Due metodi:
=> NORMALIZZAZIONE PORTA I VALORI IN UN RANGE TRA 0 ed 1

    dato un vettore X = [x1,x2,x3.....xn]
    si appllica la formula xi norm = (xi - xmin) / (xmax - xmin) va fatto per ogni elemento dell'arrai da i che va da 0 ad n

=> STANDARDIZZAZIONE PORTA LA DISTRIBUZIONE IN UNA DISTRIBUZIONE NORMALE
    ovvero in una distribuzione di valori con media centrata a 0 e deviazioen standard pari ad 1

    per ogni valore del vettore applico la formula:  xi std = (xi - xmean) / xsd

    conserva le informazioni dei valori che si discostano ma alcuni valori possono essere negativi


"""
import pandas as pd
import numpy as np

wines = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", usecols=[0, 1, 7],
                    names=['classe', 'alcol', 'flavonoidi'])
Y = wines['classe'].values
X = wines.drop('classe', axis=1).values
print(wines.describe())

# normalizziamo
wines_norm = wines.copy()  # copiamo il dataframe
features = ["alcol", "flavonoidi"]  # array delle colonne da normalizzare
to_norm = wines[features]  # sottoarray contente solo quste colonne

wines_norm[features] = (to_norm - to_norm.min()) / (to_norm.max() - to_norm.min())
print(wines_norm)

# usando numpy
from sklearn.preprocessing import MinMaxScaler

mms = MinMaxScaler()
X_norm = X.copy()
X_norm = mms.fit_transform(X_norm)
print(X_norm[:5])

# STANDARDIZZAZIONE

WINES_STD = wines.copy()
to_std = WINES_STD[features]
WINES_STD[features] = (to_std - to_std.mean()) / (to_std.std())
print(WINES_STD)

# usando numpy
from sklearn.preprocessing import StandardScaler

X_std = X.copy()
ss = StandardScaler()
X_std = ss.fit_transform(X_std)
print(X_std[:5])

# -  - ------ - -  - - - - - --  --  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from sklearn.datasets import load_boston

boston = load_boston()

X = boston.data
Y = boston.target

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

boston_df = pd.DataFrame(data=np.c_[boston['data'], boston['taget']],
                         columns=np.append(boston['feature_names'], 'TARGET'))

boston_test_df = boston_df.sample(frac=0.3)
boston_test_df = boston_df.drop(boston_test_df.index)
