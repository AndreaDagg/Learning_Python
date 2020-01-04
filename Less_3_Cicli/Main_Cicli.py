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
