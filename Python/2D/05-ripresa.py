# output - il programma dice una informazione a noi
# print("ciao")

# input - diamo noi una informazione al programma
# serve il contenitore per il messaggio
# nome = input("come ti chiami? ")
# print(f"Ciao {nome}")

####################################################
# quando si salva un numero si mette davanti int
# nascita = int(input("In che anno sei nato? "))
# anni = 2025 - nascita # operazione matematica
# print(f"Hai {anni} anni")

####################################################
# programma che mi chiede in che anno sono nato
# mi dice quanti anni ho e se ho meno di 50 anni mi dice
# sei giovane! altrimenti dice vecchiaccio
# nascita = int(input("In che anno sei nato? "))
# anni = 2025 - nascita # operazione matematica
# print(f"Hai {anni} anni")

# if anni < 50:
#     print("Sei giovane!")
# else:
#     print("Vecchiaccio!")

####################################################
# cicli for, creo un programma che ripete 5 volte
# la parola che gli dico
# parola = input("Dimmi una parola a caso: ")
# for i in range(1,5):
#     print(f"{i}.{parola}")

####################################################
# while, creo un programma che fino a quando non gli 
# dico stop, continua a chiedermi numeri

# num = input("Dimmi un numero a caso: ")
# # != significa diverso
# while num != "stop":
#     num = input("Dimmi un altro numero, oppure stop: ")

####################################################
# posso creare delle liste

spesa = ["mele", "acqua", "pane", "zucchero"]
# posso stampare i singoli elementi della lista
# print(spesa[1])

# programma che mi chiede cosa voglio aggiungere alla lista
elemento = input("Cosa aggiungo alla lista della spesa? ")

# comando per aggiungere elementi alla lista
spesa.append(elemento)
print(spesa)

# per togliere gli elementi da una lista
spesa.remove("acqua")
print(spesa)

# per mettere una lista in ordine alfabatico/numerico
spesa.sort()
print(spesa)

# stampo i valori della lista uno per riga
for i in spesa:
    print(i)