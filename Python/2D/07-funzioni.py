# funzioni sono pezzi di codice che possiamo riutilizzare che fanno
# cose che ci servono 

# bisogna prima crearle / definirle 
# def saluta():
#     print("ciao")

# e poi per farle funzionare bisogna chiamarle
# saluta()

# un funzione è come una macchinetta, ci mettiamo qualcosa dentro 
# ed esce quello che ci serve 
# le informazioni che mettiamo nella parentesi si chiamano parametri 

# def saluta(nome):
#     print(f"ciao {nome}")

# saluta("Federico")
# saluta("Matta")
# saluta("Alfonso")

# funzione che calcola l'area del rettangolo
# l'area del rettangolo si calcola base x altezza
# def area_rettangolo(base,altezza):
#     area = base * altezza
#     print(f"l'area del rettangolo è {area}")

# funzione con parametri definiti prima 
# area_rettangolo(10,2)

# base = int(input("Quanto misura la base? "))
# altezza = int(input("Quanto misura l'altezza? "))
# area_rettangolo(base,altezza)

# per spezzettare le funzioni e utilizzarle più volte tengo solo l'azione 
# che mi serve di più 

# def area_rettangolo(base,altezza):
    # il comando per far si che la funzione mi dia il risultato è return 
    # return base * altezza

# base = int(input("Quanto misura la base? "))
# altezza = int(input("Quanto misura l'altezza? "))

# metto direttamente dentro al print la funzione
# print(f"L'area del rettangolo è {area_rettangolo(base,altezza)}")

########################################################################################################################################
# creo una funzione che mi chiede un numero, poi mi chiede di quanto è lo sconto 
# in percentuale e quindi mi dice quanto andrò a pagare 

# ci servono due parametri 
# def sconto(prezzo_intero, scontato):
    # formula per calcolare il prezzo scontato 
    # valore_sconto = prezzo_intero * scontato / 100
    # prezzo_scontato = prezzo_intero - valore_sconto
    # return prezzo_scontato

# prezzo_intero = int(input("Quanto costa il prodotto? "))
# scontato = int(input("Di quanto è lo sconto? "))

# print(f"Il nuovo prezzo è {sconto(prezzo_intero,scontato)}")

########################################################################################
# programma che mi chiede il prezzo scontato, poi di quanto è lo sconto
# e mi dice quanto costava prima dello sconto 
# def prezzo_originale(prezzo_scontato, valore_sconto):
#     return prezzo_scontato / (100 - valore_sconto) * 100

# prezzo_scontato = int(input("Quanto costa il prodotto scontato? "))
# valore_sconto = int(input("Di quanto era lo sconto? "))

# print(f"il prezzo iniziale era: {prezzo_originale(prezzo_scontato, valore_sconto)}")

########################################################################################
# Creo un programma che mi chiede il prezzo di un prodotto senza IVA
# calcola quanto è il valore dell'IVA aggiunto al prezzo
# calcola il valore finale del prodotto

# def calcolo_iva(prezzo_noiva, iva):
    # valore_iva = prezzo_noiva * iva / 100
    # prezzo = prezzo_noiva + valore_iva
    # sputo fuori dalla funzione entrambi i valori che mi servono 
    # return valore_iva, prezzo

# float serve per i numeri con la virgola 
# prezzo_iva = float(input("Qual è il prezzo del prodotto senza IVA? "))
# iva = float(input("Quanto è l'IVA su questo prodotto? "))

# quanto andiamo a chiamare la funzione possiamo usare entrambi i risultati che 
# la funzione ci resituisce con return 

# assegno a due elementi i valori usciti dalla funzione 
# iva_aggiunta, prezzo_finale = calcolo_iva(prezzo_iva, iva)

# uso i due elementi per stampare i valori 
# print(f"L'iva aggiunta sul tuo prezzo è di: {iva_aggiunta}")
# print(f"Il prezzo finale è quindi di: {prezzo_finale}")

########################################################################################

# Creo una funzione che calcola quanti km posso fare in macchina,
# il programma deve chiedermi quanti litri di benzina ho fatto e quanti km con 
# un litro fa la mia macchina 

# def km_totali(litri, consumo):
#     viaggio = litri * consumo
#     return viaggio

# litri = float(input("Quanti litri hai fatto? "))
# consumo = float(input("Quanti km fa la tua macchina al litro? "))

# print(f"Puoi fare {km_totali(litri,consumo)} km")

# prova a modificare la funzione affinchè chieda quanto hai speso al benzinaio,
# considerando che 1 litro costa 1.65 euro, fai in modo che calcoli 
# quanti litri hai fatto e da questa informazione quanti km restano





