'''
Per definire una funzione si usa @def e poi nome funzione eventuali parametri tra parentesi () ed infine i due punti :

'''


def capture_area(base, altezza):
    return base * altezza / 2


b = 5
h = 5
area = capture_area(b, h)
print(area)


# I paramtri con default vanno sempre messi dopo quelli che non li hanno
def funzione_con_valore_default(lista, supermercato="Conad"):
    for i, j in enumerate(lista):
        if (i == 2):
            print(F"{i}) {j} Sup: Decò")
            continue
        print(F"{i}) {j} Sup: {supermercato}")


# In questo modo non cambio il parametro supermercato che resterà di default
funzione_con_valore_default(["carne", "caciocavallo", "acqua"])
print("-- Modifico il parametro di default --")
# In questo modo non cambio il parametro supermercato che resterà di default
funzione_con_valore_default(["carne", "caciocavallo", "acqua"], "Coop")

'''@RETURN Fnzione con valore di ritorno'''
print("\n-- Return --")

def somma(a, b):
    c = a + b
    return c

a = 2
b = 4
print(F"Somma di {a} + {b} =", somma(a, b), "\n")


