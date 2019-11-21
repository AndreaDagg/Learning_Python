print("Hola")
print(10 - 2.2)
# divisione solo intero
print(10 // 3)

# potenza
print(2 ** 2)

# input da tastiera
# salviamo l'input tramite variabili che sono non tipizzate
name = input("Come ti chiami? ")
print(name)

# Vediamo il tipo della variabile
var = "ciao"
type(var)
var = 3.5
var = True
var = False

# cast
eta = 10
var = str(eta)

# Gestire eccezioni cast da stringa a intero sbagliata
# Attenzione all'intentazione perché non abbiamo le parentesi
num = input("Inserisci un numero:")
try:
    print(type(num))
    num = int(num)
    print("Il numero inserito è: ", num)
except ValueError:
    print("Il dato non è un numero")

# Formattazione
print("Nome %s numero: %d " % (name, num))
print("Nome {name} numero: {num}".format(name=name, num=num))
print(F"Nome {name} numero: {num}")
