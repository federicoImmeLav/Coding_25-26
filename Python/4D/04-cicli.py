# programma che mi chiede un numero, 
# lo moltiplica per 5,
# se il numero che ottengo è maggiore di 60 mi dice: "maggiore di 60"
# altrimenti mi dice "minore di 60"

# chiedo un num quindi metto int davanti
# numero = int(input("Dimmi un numero "))

# numero = numero * 5

# if numero > 60:
#     print(f"{numero} è maggiore di 60")
# else:
#     print(f"{numero} è minore di 60")
###########################################################################
# programma che stampa una serie di numeri partendo da 37 e arrivando a 75
# for i in range(37,76):
#     print(i)
###########################################################################
# programma che stampa solo i numeri divisibili (%) per 3 tra 45 e 189
# for i in range(45,190):
#     if i % 3 == 0: # se diviso per tre non da resto
#         print(i)
###########################################################################
# programma che mi chiede numeri fino a quando non dico stop
# punto di partenza
# numero = input("Dimmi un numero ")

# while numero != "stop":
#     numero = input("Dimmene un altro ")
###########################################################################
# programma che mi chiede un numero, 
# mi chiede se voglio andare avanti dopo aver detto il numero
# mano a mano che vado avanti somma i numeri che gli dico
# alla fine mi dice il risultato
# numero = int(input("Dimmi un numero: "))
# avanti = input("Vuoi andare avanti? (si/no): ")
# a = numero

# while avanti != "no":
#     numero = int(input("Dimmi un altro numero: "))
#     avanti = input("Vuoi andare avanti? (si/no): ")
#     a = a + numero # sommo i numeri che mi dice

# print(f"La somma dei numeri che mi hai detto è: {a}")
#####################################################################
# programma che mi chiede animali fino a quando non indovino 
# quello giusto che è il pinguino
soluzione = "pinguino"

animale = input("Indovina l'animale che sto pensando: ")
# fino a quando rispondo un animale che non è pinguino, continua 
# a chiedermene altri 
while animale != soluzione:
    animale = input("Sbagliato, riprova (vive al freddo): ")

print("Bravo! Hai indovinato")