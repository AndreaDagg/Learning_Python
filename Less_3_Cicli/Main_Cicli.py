# Ciclo  FOR
num = int(input("Fino a quale numero?"))
for i in range(0, num):
    print(i)

# Swapping senza la variabile d'appoggio
a = "cane"
b = "gatto"
a, b = b, a

# Ciclo for per la successione di Fibonacci

num = int(input("Quanti numeri di Fibonacci vuoi stampare?"))

fib_num = 0
next_fib_num = 1

for i in range(0, num):
    fib_num, next_fib_num = next_fib_num, next_fib_num + fib_num,

    print("%d numero di Fib = %d" % (i + 1, fib_num))

# Ciclo for con una lista
shopping_list = ["carne", "latte", "carote", "riso basmati", "sapone"]
for i in range(len(shopping_list)):
    print("%d) %s" % (i + 1, shopping_list[i]))

# Ciclo for con una lista con iterazione diretta
# Iteriamo sulla liata e 'j' conterrà l'i-esimo elemento della lista solo con 'j' perdiamo però l'indice
# per tornare ad averlo possiamo aggiungerlo 'i' con eneumerate

shopping_list = ["carne", "latte", "carote", "riso basmati", "sapone"]
for i, j in enumerate(shopping_list):
    print("%d - %s" % (i + 1, j))

# Ciclo while

n = int(input("Fino a quanto vuoi contare?"))

i = 0
while (i < n):
    if (i % 3 == 0):  # se i è multiplo di 3
        i += 2  # salto l'iterazione (non stampo)
        continue  # esco dall'iteraizone
    elif (i >= 25):
        break  # esco dal ciclo
    print(i)
    i += 2

#IF e Operatori logici

if (n<0):
    print("%d non è un numero positivo")
elif (n % 2 == 0):
    print("%d è un numero pari")
else:
    print("%d è un numero dispari")

1 == 4 and 2 == 2
1 == 4 or 2 == 2
not 2 ==1