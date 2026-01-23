# dizionari sono evoluzione delle 
# ho una lista della spesa
# voglio fare che il programma mi chiede altri elementi
# fino a quando non dico stop
# questi elementi vengono aggiunti alla lista
# quando dico stop viene stampata
# spesa = ["acqua", "farina", "pane"]

# punto di partenza
# ingrediente = ""

# chiedo il primo ingrediente
# ingrediente = input("Cosa aggiungo alla lista? ")

# while ingrediente != "stop":
    # aggiungo elemento alla lista
    # spesa.append(ingrediente)
    # chiedo un altro ingrediente
    # ingrediente = input("Cosa aggiungo alla lista? ")

# per stampare tutti gli elementi della lista uno per volta si
# usa for
# for i in spesa:
    # print(i)

##########################################################################
# dizionario 
# insieme di informazioni che riguardano la stessa cosa
# persona = {
#     "nome": "Federico",
#     "cognome":"Pozzi",
#     "età":30
# }

# registro = [
#     {"nome":"Roberto", "cognome":"Gianni"},
#     {"nome": "Hossam", "cognome":"Elsayad"},
# ]

# spesa = [
#     {"cosa":"farina", "quanto":5},
#     {"cosa": "zucchero", "quanto": 3}
# ]
##########################################################################
# creo lista e nome vuoti
lista = []
#chiedo la prima volta per avviare il while
nome = input("Cosa aggiungo alla lista? ")

# while che mi chiede fino a quando non dico stop cosa e quanto,
# aggiunge cosa e quanto come nuovo elemento della lista
while nome != "stop":
    quanto = int(input("Quanto ne vuoi? "))
    # creo il dizionario con queste due informazioni
    elemento = {"cosa": nome, "quantità":quanto}
    # aggiungo il dizionario alla lista della spesa
    lista.append(elemento)
    # chiedo alla fine così se faccio stop il while non riparte
    nome = input("Cosa aggiungo alla lista? ")

# creare una funzione che vada a prendermi l'informazione secondo cui voglio
# ordinare la lista
def chiave_ordine(elemento):
    return elemento["cosa"]
# per mettere in ordine uso sort e dentro alle parentesi si sort specifico
# in base a cosa devo ordinare
lista.sort(key = chiave_ordine)

# stampa ogni elemento della lista per riga
for i in lista:
    print(i)


