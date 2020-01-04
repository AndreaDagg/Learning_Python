# Moduli
"""
Un modulo si deve trovare o nella stessa directory
Per importarlo dobbiamo usare import
"""
import Less_5_Moduli.Script

print(Less_5_Moduli.Script.hello_Word())

import Less_4_Funzioni.Main_Funzioni

# print(Less_4_Funzioni.Main_Funzioni.Triangle.print_inf())

# Possiaqmo accedere alla specifica classe senza ripetere il modulo
from Less_4_Funzioni.Main_Funzioni import triangle

triangle.print_inf()

import os

os.getcwd()

import datetime

datetime.datetime.now()

# Calcoliamo quanto impiega a calcolare la potenza
from time import time

n = 2
pow = 10
n_pow = n

tick = time()

# Il trattino si u sa quando nel for non si usa l'indice
for _ in range(pow):
    n_pow *= n

print("Durata:%f " % (time() - tick))

# Chiamta con alias
from math import pow as pow_alias

n = 2
pow = 10
n_pow = n

tick = time()

pow_alias(n, n_pow)

print("Durata:%f " % (time() - tick))

"""
Dobbiamo installare pip per poter utilizzare librerie. Pip serve per gestire i pacchetti e si installa da terminale
ad esempiuo per installare numpy una libreira per il calcolo scientifico
pip install numpy

Aggiornare un pacchetto: pip install <Name> --upgrade
Rimuovere: pip unistall <Name> 
"""
import numpy as np
#numpy è ottimizzata su matriciu e array
np.power(n, n_pow)
