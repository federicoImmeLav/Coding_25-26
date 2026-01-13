# if e for

# creo un programma che mi chiede 3 voti 
# e mi dice la media dei voti

# python mi chiede i voti
# voto1 = int(input("Dimmi un voto che hai preso "))
# voto2 = int(input("Dimmene un altro "))
# voto3 = int(input("Dimmi anche il terzo "))

# # calcolo la media dei tre voti
# media = (voto1 + voto2 + voto3)/3

# # scrivo il risultato nel terminale
# print(f"La media dei tuoi voti è: {media}")

# # aggiungo che se la media dei voti è minore di 60
# # mi dice che sono insufficiente
# # se è tra 60 e 80 mi dice che sono stato bravo
# # se è sopra 80 mi dice che sono bravissimo
# # con if si parte dal più grande
# if media >= 80:
#     print("La tua media è sopra l'80, sei bravissimo/a")
# elif media < 80 and media >= 60:
#     print("La tua media è tra 60 e 80: bravo!")
# elif media < 60:
#     print("Hai preso meno di 60: andrà meglio la prossima volta")

################################################################################
# per ripetere le cose quante volte voglio io
# si usa for, funziona indicando una variabile
# che ogni volta che fa l'azione che gli dico,
# aumenta di 1, fino a quando non arriva al valore
# indicato
# for i in range(50):
#     print(i)
# il for funziona passando la variabile attravero
# quello che c'è dopo
# for i in "Simone":
#     print(i)

# i dati in py sono stringhe e numeri
# esistono anche le liste, che sono un insieme 
# di stringhe, numeri o entrambi 

# # lista di stringhe
# spesa = ["Acqua", "Farina", "Mele", "Caramelle"]
# # lista di numeri
# voti = [1, 10, 50, 30]
# # lista mista
# misto = [2, "Simone", "Tavolo", 50]

# spesa = ["Acqua", "Farina", "Mele", "Caramelle"]
# print(spesa)
# # posso aggiungere elementi a una lista con append
# spesa.append("Pollo")
# print(spesa)
# # posso rimuovere un elemento con remove
# spesa.remove("Farina")
# print(spesa)
###########################################################

# spesa = ["Acqua", "Farina", "Mele", "Caramelle"]
# for i in spesa:
#     print(i)

###########################################################
# creo un programma che mi chiedeedien 5 ingrti per la 
# ricetta che voglio fare e quando finisco di dirglieli
# me li stampa in ordine 

# # creo la lista della spesa vuota
# spesa = []
# # imposto il for perchè ripete per 5 volte
# for i in range(5):
#     ingrediente = input("Che ingrediente ti serve? ")
#     spesa.append(ingrediente)
# # metto un comando fuori dal for, questo comando verrà eseguito
# # dopo tutto il for 
# print(spesa)
# # metto la lista in ordine alfabetico
# spesa.sort()
# # stampo la lista una parola per riga
# for i in spesa:
#     print(i)
#####################################################################
# esiste un comando che ripete una azione fino a quando non 
# si verifica la condizione che lo fa fermare
# cioe: ripeto fino a quando non succede qualcosa
# si chiama while

# indico il punto di partenza
# i = 0
# while i < 50: # indico la condizione
#     print("ciao")
#     i = i + 1

# programma che mi chiede un numero fino a quando non dico stop
# num = input("Dimmi un numero ")
# while num != "stop":
#     num = input("Dimmi un altro numero (stop per fermare) ")
####################################################################

# programma che mi chiede numeri fino a quando non dico stop, 
# quando dico stop mi dice la somma di tutti i numeri che ho detto 

# creo contenitore per la somma
somma  = 0
num = input("Dimmi un numero ")

while num != "stop":
    somma = somma + int(num)
    num = input("Dimmi un altro numero (stop per fermare) ")
# metto quello che deve succeder quando il while finisce
print(f"La somma di tutti i numeri che mi hai detto è: {somma}")