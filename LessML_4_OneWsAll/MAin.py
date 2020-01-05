import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

"""
Classificiazione One Vs All di numeri scritti a mani 
"""
from sklearn.datasets import load_digits

digits = load_digits()

X = digits.data
Y = digits.target

print(X.shape)
print(np.unique(Y))  # Visualizza le classi del dataset

for i in range(0, 10):
    pic_matrix = X[Y == i][0].reshape([8, 8])
    plt.imshow(pic_matrix, cmap="gray")
    plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

"Essendo img conviene normalizzare le colonne in modo da avere una distribuzione che va da 0 ad 1 piuttosto che da 0 a 255"
from sklearn.preprocessing import MinMaxScaler

mms = MinMaxScaler()
X_train = mms.fit_transform(X_train)
X_test = mms.transform(X_test)

lr = LogisticRegression()
lr.fit(X_train, Y_train)

Y_pred = lr.predict(X_test)
Y_pred_prob = lr.predict_proba(X_test)

print("ACCURACY: " + str(accuracy_score(Y_test, Y_pred)))
print("LOG LOSS: " + str(log_loss(Y_test, Y_pred_prob)))

"""
Matrice di confusione ci fa vedere su quali classi il modello ha commesso piú errori
Mostra ome gli esempi sono stati classificati, le colonne rappresentano le classi predette
le righe le classi corrette. 

Es. in valore 2 alla 5 colonna della 9 riga indica che 2 img rappresentati un 9 sono state rappresentati con 5
"""
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(Y_test, Y_pred)
print(cm)

# rappresentiamolo con heatmap
import seaborn as sns

plt.figure(figsize=(9, 9))
sns.heatmap(cm, annot=True, cmap="Blues_r", linewidths=.5, square=True)
plt.ylabel('Classe corretta')
plt.xlabel('Classe predetta')
plt.show()
