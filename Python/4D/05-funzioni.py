# # # # def area(b,h):
# # # #     return b * h 

# # # # print(area(4,5))
# # # # print(area(2,53))
# # # # print(area(6,10))

# # # nome = input("come ti chiami? ")
# # # def saluta(nome):
# # #     print(f"ciao {nome}")
    
# # # saluta(nome)

# # # creo un programma con una funzione che mi chiede il prezzo attuale
# # # di un prodotto, di quanto è lo sconto in percentuale 
# # # mi risponde dicendomi quanto costava prima di essere scontato
# # def prezzo(prezzo, sconto):
# #     return prezzo * 100 / (100-sconto)

# # spesa = int(input("qual è il prezzo del prodotto? "))
# # sconto = int(input("di quanto è lo sconto? "))

# # risultato = prezzo(spesa, sconto)
# # print(f"il prezzo originale era di {int(risultato)} euro ")


# # risparmio = risultato - spesa 
# # print(f"stai risparmiando {int(risparmio)} euro ")


# # creo un programma con una funzione che mi chiede quanti km fa 
# # la mia macchina con un litro, mi chiede quanti litri ho fatto
# # con l'ultimo pieno.
# # il programma mi risponde dicendomi quanti km posso fare con la
# # benzina che ho

# def kmtero(benzina, km):
#     return km * benzina

# benzina = int(input("quanti litri ho nel serbatoio? "))
# km = int(input("quanti km faccio con un litro? "))
# totale = kmtero(benzina, km)

# print(f"i km che puoi fare in totale sono di {int(totale)} km ")
# funzione che ci chiede un numero di minuti
# calcola quante ore 
# calcola quanti minuti avanzano
# scrive la frase: sono tot ore e tot minuti

# def orologio(minuti): 
#     ore = minuti / 60 
#     restanti = minuti % 60
#     return ore, restanti
# minuti = int(input("quanti minuti? "))

# o,m = orologio(minuti)
# print(f"le ore sono:{o}, i minuti: {m}")
# funzione che prende una lista di numeri e mi restituisce la lista con i numeri 
# moltiplicati per 2 
lista = [4,7,5,9,11]

def doppio(numero):
    return numero * 2

for i in lista:
    print(i)
    print(doppio(i))
    
print(doppio("methsala"))
