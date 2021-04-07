# Python mette a disposizione 4 tipi di dati per rappresentare elementi
# --- LISTE ----

# Si insieriscono gli elementi tra le parentesi quadre e si indirizzano come con gli array
# si può prendere solo una parte della lista con l'oreazione di slicing

my_list = [10, 5, 6, 7, 3, 2, 5, 67]

# indexing
my_list[1]
my_list[-1]  # stampa 67

# slicing
my_list[0:3]  # dal primo al terzo elemento
my_list[:3]
my_list[2:]  # dal secondo in poi
my_list[::1]  # aggiungendo un terzo paramnetro possiamo insiscare se leggere da sx a dx
my_list[::-1]  # da dx a sx

# modificare un valore in una lista

my_list[0] = 100
my_list[-2:] = [200, 90]  # modifichiamo gli ultimi due valori

# verifica se un valore è presente in lista si una in

animals = ["cani", "gatto", "topo"]
"uomo" in animals  # return false
"gatto" in animals

# rimozione per valore:
animals.remove("gatto")

# estrazione per indice:
animals.pop(1)
print(animals)

# aggiungere elementi in coda
animals.append("leone")
print(animals)
# aggiungiamo un elementoi in una specifica posisizione spostando anche quelli che già ci sono
animals.insert(1, "giraffa")
print(animals)

# ---- TUPLE ----
# Le tuple non sono modificabili una volta definite. Si definiscono tramite parentesi tonde

my_tuple = (10, 5, 6, 3, 9)
my_tuple[1]
my_tuple[:3]

# le tuple possono contenere tipi diversi al loro interno
my_tuple_2 = (10, "ciao", False, 10.5, 10)

# ottenere l'indicie di un elemento di una lista o tupla
my_tuple_2.index("ciao")

# conta gli elementi
my_tuple_2.count(10)

# lenght
len(my_tuple)

hello = "hello python"
len(hello)
hello[4]

# ---- SET ----
# Insieme di elementi unici non ordinati quindi non può contenere due elementi uguali
# si crea tra parentesi graffe

my_set_nomi = {"Andrea", "Francesco", "Emanuela", "Luca", "Carlo"}

my_set_nomi.add("Pippo")
print("Prima della rimozione: ")
print(my_set_nomi)

my_set_nomi.remove("Pippo")
print("Dopo la rimozione: ")
print(my_set_nomi)

my_set_nomi.pop()  # Rimuove casualmente un elemento perché l'ordine è casuale nel SET e quindi non si sa chi sta in fondo

# svuotare il set
my_set_nomi.clear()

# convertire una lista in SET e viceversa
lista_nomi = ["Andrea", "Francesco", "Emanuela", "Luca", "Carlo"]
set_nomi = set(lista_nomi)
lista_nomi = list(set_nomi)

# ---- FROZENSET ----
''' Il set congelato è solo una versione immutabile di un oggetto set Python . Mentre gli elementi di un set possono
    essere modificati in qualsiasi momento, gli elementi del set congelato rimangono gli stessi dopo la creazione.
    Per questo motivo, i set congelati possono essere utilizzati come chiavi nel Dizionario o come elementi di un altro set. 
    Ma come gli insiemi, non è ordinato (gli elementi possono essere impostati su qualsiasi indice). '''

names = frozenset(set_nomi)

# ---- DIZIONARI ----
# Permettono di immagazzinare i dati in strutture key value

dict = {"latte": 3,
         "riso": 2,
         "carne": 34}

dict["latte"]  # da 3
dict["latte"] = 2
dict["cereali"] = 1  # aggiunge l'elemento
dict["yogurt"] = {"fragola": 2, "bianco": 4}

dict["yogurt"]["fragola"] = 23

dict.keys()  # ritorna tutte le chiavi
keys = list(dict.keys())
values = list(dict.values())

print("Dizionari \nsolo le key: ",keys)
print("solo i valori: ", values)

print("dizionario: ", dict)
