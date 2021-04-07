# Programmazione ad Oggetti
# definiamo la classe ed il metodo __init__ è il costruttore che verrà chiamato automaticamente
# il piromo parametro di un metodo di una classe è self

'''
Classi:     Ci consentono di raggruppare variabili e funzioni per riutilizzarle
Istanza:    Ogni elemento creato attraverso il modello della classe

si usa l'attributo @class ed è buona norma mettere la prima lettera del nome della classe maiuscola
Metodo __init__ inizializzatorre / costruttore costruire gli oggetti
@__init__ inizializza e attiva le proprietà di ciascun oggetto / istanza self creato

@self Quando creiamo dei metodi all'interno della classe passiamo il prametro @sefl (se stesso)
@self rappresenta l'istanza, ogni singolo oggetto creato dalla classe, rappresenta quindi l'oggetto a cui devono essere associate i parametri passati nella funzione
La classe rappresenta il modello generico, @self rappresenta una referenza a ciascun oggetto creato dalla classe
'''
''' Quindi per ciascuno dei self inizializzati ogni self avrà associato il nome, il cognome e corso che abbimo passato 
come paramentro e vengono dette variabili di istanza '''


class Studente:
    ore_settimanali = 36  # variabile di classe
    corpo_studentesco = 0  # variabile per il conteggio degli oggetti di tipo studenti totali creati

    def __init__(self, nome, cognome, corso):
        self.nome = nome
        self.cognome = cognome
        self.corso = corso
        Studente.corpo_studentesco += 1  # incremento perché ho inizializzato un nuovo oggetto

    def scheda_personale(self):
        return F"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso: {self.corso}\n Ore:{self.ore_settimanali}\n"


# Creiamo due istanze della classe Studente
# Dalla stampa otterremo due oggetti di tipo studente e l'inidirizzo di memeoria associato all'oggetto creato

studente_uno = Studente("Andrea", "DAgg", "inf")
studente_due = Studente("Luca", "Rossi", "Bio")

print("--- Print delle istanze delle classi ---\n", studente_uno, studente_due)

# Utilizzaimo il metodo scheda personale per stampare le infomazioni relativa ad ogni oggetto
'''
DUE METODI
1 - Si utilizza il metodo self nel metodo scheda per andare a indicizzare le variabili di istanza 
2 - Chiamiamo il metodo della calsse e poi passiamo l'oggetto, @self rappresenterà l'istanza dell'oggetto passato 
'''
print(studente_uno.scheda_personale())
print(Studente.scheda_personale(studente_due))

'''
Ogni classe dispone di attributi propri le variabili di istanza definite tramite self 
Le variabili di classe sono attributi condivise tra tutte le istanze della classe ceh quidni è inutile passare ogni volta come parametro
Ci accediamo in due modi: 
- richimando semplicmente           NomeClasse.Variabilediclasse
- oppure tramite istanza stessa     self.VariabilediClasse

Modifichiamo il valore della varibile dell'oggetto specifico e stampiamo il nuovo valore
'''
studente_due.ore_settimanali += 4
print("CAMBIO VARIABILE DI CLASSE\n", Studente.scheda_personale(studente_due))
print("Numero Studenti: ", Studente.corpo_studentesco, "\n")


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

# ritorna i metodi presnti in una classe
help(triangle)
