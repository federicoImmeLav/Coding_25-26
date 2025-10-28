# if elif - se, allora
# while - mentre, succedono delle cose mentre qualcosaltro è vero
# for - per, per ogni condizione fai qualcosa

# programma che mi chiede un numero e mi dice se è maggiore 
# o minore di 30

# per leggere un numero devo mettere int davanti
# numero = int(input("Dimmi un numero a caso "))
# print(numero)

#si scrive la condizione dopo if seguita dai : quello che deve fare
# il mio if si scrive indentato, altrimenti non va 
# if numero >= 30:
#     print("Il numero è maggiore di 30")
# elif numero < 30:
#     print("Il numero è minore di 30")

# il mio programma ora deve dirmi se il numero è minore di 10 
# se è maggiore di 10 e minore di 30
# se è maggiore di 30
# quando faccio gli if devo andare dal generale al particolare
# if numero < 10:
#     print("minore di 10")
# elif numero >= 30:
#     print("maggiore di 30")
# elif numero >= 10:
#     print("maggiore di 10 e minore di 30")

#a = 10 #numero
#nome = "Federico" #stringa
# liste 

# print(nomi[2])
#le liste possono essere di stringa ma anche di numeri
# numeri = [20, 24, 35, 71]

# ciclo for serve a ripetere una azione quante volte voglio
# per ogni nome presente nella lista, scrivimelo
# nomi = ["Alfonso", "Kevin", "Emanuele", "Lorenzo"]
#per ogni valore di a che sta dentro a nomi 
# finchè ci sono valori dentro a nomi
# for a in nomi: 
#     print(a)

#finchè i parte da 0 e arriva a 5, stampa il valore di i
# for i in range(0,5):
#     print(i)


#while è un comando che ripete una azione fino a 
# quando non si verifica la condizione che la stoppa 
# i = 1
# while i < 5:
#     print("ciao")
#     i = i + 1 
    #devo ricordarmi di mettere sempre la condizione di stop

#Fino a quando non rispondiamo giusto continua a chiedermelo
nome = input("Come ti chiami? ")

while nome != "Federico":
    nome = input("Hai sbagliato, Come ti chiami? ")

print("hai risposto giusto!")
