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


funzione_con_valore_default(["carne", "caciocavallo", "acqua"])
