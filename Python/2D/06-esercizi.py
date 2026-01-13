# 1. Crea un programma che ti chiede 3 numeri
# num1 = int(input("Dimmi un numero: "))
# num2 = int(input("Dimmene un altro: "))
# num3 = int(input("Dimmi l'ultimo: "))

# # li somma
# somma = num1 + num2 + num3

# # stampa il risultato
# print(f"La somma dei numeri è: {somma}")

################################################################
# 2. Crea un programma che mi chiede un numero
# mi chiede un altro numero 
# mi dice quanto fa la somma dei due numeri 
# continua a chiedermi numeri e a sommarli fino a quando non dico stop

# num = int(input("Dimmi un numero: "))
# numero_chiesto = int(input("Dimmi un altro numero: "))

# while numero_chiesto != "stop":
#     num = num + int(numero_chiesto)
#     print(f"La somma fino ad ora è {num}")
#     numero_chiesto = int(input("Dimmi un altro numero, per fermare dimmi stop: "))

# print(f"Ti sei fermato a {numero_chiesto}")

##################################################################################
# 3. Creo un programma che mi chiede che cosa voglio 
# mettere in una lista della spesa. 
# Mi chiede un elemento per volta e ogni volta
# lo aggiunge alla lista quando arrivo alla fine 
# della lista, gli dico stop e lui smette di chiedere
# mette in ordine alfabetico la lista della spesa
# e me la stampa uno elemento per riga

# lista = []

# print("Ti creo una lista della spesa.")
# elemento = input("Dimmi un ingrediente: ")

# while elemento != "stop":
#     lista.append(elemento) # aggiungo alla lista
#     elemento = input("Dimmene un altro oppure stop: ")

# # quando finisco di dire gli elementi della lista
# # metto in ordine la lista
# lista.sort()
# print("La tua lista della spesa è: ")
# # stampo la lista uno per riga
# for i in lista:
#     print(i)

