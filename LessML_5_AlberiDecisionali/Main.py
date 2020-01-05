import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score

titanic = pd.read_csv("http://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
titanic.info()
titanic.head()

titanic = titanic.drop("Name", axis=1)
titanic = pd.get_dummies(titanic)  # Why not encoding che si applicherà sulla proprietà sex
print(titanic.head())

x = titanic.drop("Survived", axis=1).values
y = titanic["Survived"].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x.shape)

"""
Costruiamo l'albero da sklearn, e nell'istanziamento tramite criterion impostiamo la metrica dell'impurità Gini o Entropi
"""
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(criterion="gini", max_depth=6)
tree.fit(x_train, y_train)
y_pred_train = tree.predict(x_train)
y_pred = tree.predict(x_test)

accuracy_train = accuracy_score(y_train, y_pred_train)
accuracy_test = accuracy_score(y_test, y_pred)

print("ACCURACY: TRAIN=%.4f TEST=%.4f" % (accuracy_train, accuracy_test))
"""
Abbiamo un accuratezza del TRAIN del 0.9806 e TEST del 0.7528 
queste metriche indicano che l'albero soffre di overfitting ed è dunque troppo complesso quuindi troppo profondo, 
quindi porviamo a ridurre la profondità tornando nell'inizzializzazioen dell'albero e passando il paramentro max_depth 
"""

from sklearn.tree import export_graphviz

dotfile = open("tree.dot", "w")
export_graphviz(tree, out_file=dotfile, feature_names=titanic.columns.drop("Survived"))
dotfile.close()
