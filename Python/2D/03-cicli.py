# # for, while e differenze
# nome = input("Come ti chiami? ") #input dell'utente
# print(nome) #output del pc

# # stringhe vs numeri
# a = 0 # numero
# b = "Alfonso" # stringa

# # if elif
# if a == 0:
#     print("ciao")
# elif a == 1:
#     print("buongiorno")

# for e while servono a fare delle azioni ripetute automaticamente
# for ripete le azioni che gli diciamo finchè 
# siamo dentro a un range di azione
# for i in range(0,5):
    # print("ciao")

# for i in range(0,50):
#     print(f"Il mio numero preferito è {i}")

# programma che prende una lista di nomi e stampa il saluto 
# a ciascun elemento della lista
# lista:
# nomi = ["Emanuele", "Lorenzo", "Alfonso", "Ryne", "Shevan","Santiago", "Ammar"]

# for i in nomi:
#     print(f"Ciao {i}")

# stampo tutte le lettere di una scritta
# for i in "Ammar":
#     print(i)


# while serve a ripetere qualcosa finchè una condizione non si verifica
# i = 0
# while i < 7:
#     print("ciao")
#     # dobbiamo inserire anche la condizione che cambia per farlo fermare altrimenti
#     # va avanti all'infinito
#     i = i + 1

# programma che mi chiede quanto fa 5 + 5 fino a quando non rispondo giusto
# risultato = int(input("Quanto fa 5 + 5? "))
# while risultato != 10:
#     risultato = int(input("Sbagliato, quanto fa? "))
# # qui metto quello che deve dirmi quando faccio giusto
# print("Good boy!")

# programma che mi chiede un numero a caso tra 15 e 20
# sommo il numero che mi ha detto a 5 e stampo il risultato
# dopo averlo chiesto, stampa i 10 numeri precedenti in ordine decrescente
# i = int(input("Dimmi un numero a caso tra 15 e 20 "))
# # int serve a convertire la stringa in numero
# print(i)
# for a in range(0,10):
#     print(i)
#     i = i - 1
