# while e i dizionari
# ripetere fino a quando non succede qualcosaltro

# a = 0
# while a < 5: 
#     print("ciao")
#     a = a + 1

# fai un codice che chiede un numero all'utente
# fino a quando non indovina il 17
# quando indovina digli bravo

# condizione iniziale
# num = int(input("Indovina il numero che sto pensando "))

# while num != 17:
    # num = int(input("Riprova "))

# cosa fa quando il while viene fermato
# print("bravo, hai indovinato!")

# faccio lista della spesa, codice mi chiede gli ingredienti
# li salva in una lista e alla fine me li stampa
# in ordine alfabetico

# creo la lista vuota
# spesa = []

# punto di partenza: chiedo il primo ingrediente
# ingrediente = input("Dimmi il primo ingrediente ")

# creo il while (se dico stop si ferma)
# while ingrediente != "stop":
    # aggiungo ingrediente alla lista
    # spesa.append(ingrediente)
    # chiedo un altro ingrediente
    # ingrediente = input("Dimmi il prossimo ingrediente ")

# quando il while si ferma succede che
# metto la lista in ordine alfabetico (sort)
# spesa.sort()

# stampo gli elementi della lista uno per riga con for
# for i in spesa:
    # print(i)

#####################################################################################
# creo un programma che mi fa fare una lista della spesa
# chiedendomi prima gli ingrediente e poi quanti ne voglio
# dopo avermi chiesto le info, le salva in un dizionario (oggetto)
# ogni oggetto sta dentro una lista, alla fine mi stampa la lista

# creo la lista vuota
lista = []
# creo il primo ingrediente
ingrediente = input("Dimmi il primo ingrediente ")

# while ingrediente diverso da stop
while ingrediente != "stop":
    # chiedo quantità dell'ingrediente
    quantità = int(input("Quanti ne vuoi? "))

    # creo l'elemento della lista della spesa
    # che abbia sia ingrediente che quantità
    elemento = {"nome":ingrediente, "quanto":quantità}

    # metto l'elemento nella lista
    lista.append(elemento)

    # chiedo il prossimo ingrediente
    ingrediente = input("Dimmi un altro ingrediente ")

# stampo la lista un elemento per riga
for i in lista:
    print(i)