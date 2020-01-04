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


# Programmazione ad Oggetti
# definiamo la classe ed il metodo __init__ è il costruttore che verrà chiamato automaticamente
# il piromo parametro di un metodo di una classe è self

class Triangle:
    """
    Questa classe rappresenta un tirangolo: descrivo la classe
    """

    def __init__(self, a, b, c, h):
        self.a, self.b, self.c, self.h = a, b, c, h

    def area(self):
        return self.b * self.h / 2

    def perimeter(self):
        return self.a + self.b + self.c

    # Metodo che utilizzaa altri metodi
    def print_inf(self):
        print(F"Area {self.area()}")
        print(F"Perimetro {self.perimeter()}")


triangle = Triangle(3, 5, 6, 7)
# triangle.area(3, 5)
# triangle.perimeter(3, 5, 8)
triangle.perimeter()
triangle.area()
triangle.print_inf()

#ritorna i metodi presnti in una classe
help(triangle)