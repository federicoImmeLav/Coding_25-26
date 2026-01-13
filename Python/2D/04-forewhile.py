# # esercizio 1 della verifica
# # funzione di input così che l'utente può scrivere
# nome = input("Come ti chiami? ")
# eta = input("Quanti anni hai? ")

# # funzione di output, python che ci dice delle cose
# print(f"Ti chiami {nome} e hai {eta} anni")


# # esercizio 2 della verifica
# # stampa i numeri da 1 a 10
# # for in range ripete una azione tante volte quanti sono i numeri scritti
# for i in range(10):
#     print(i + 1) # stampo i numeri partendo da 1 e non da 0
# # chiedere all'utente un numero tra 5 e 10
# # con i numeri si usa int
# numero = int(input("Dimmi un numero tra 5 e 10 "))
# # scrivi i 6 numeri successivi a quello che ti dice
# for i in range(6):
#     print(numero + 1 + i)


# for serve per ripetere le cose un numero finito di volte
# while serve per ripetere le cose fino a quando non succede altro
# for i in range(5):
#     print("ciao")

# a = 0
# while a < 5:
#     print("ciao")
#     a = a + 1

#####################################################################

# # creo un programma che mi chiede di inserire il mio indirizzo
# # email e fino a quando non lo scrivo giusto continua a richiederlo

# # 1. definisco il punto di partenza, dico al programma
# # qual è la mail corretta
# mail = "federico.pozzi@immaginazioneelavoro.it"

# # 2. chiedo all'utente la mail
# account = input("Scrivi il tuo indirizzo email: ")

# # 3. costruisco il while in modo tale che finchè metto la mail
# # sbagliata continua a richiedermela
# while account != mail:
#     print("hai sbagliato!")
#     account = input("riprova: ")

# # 4. una volta che metto la mail giusta esco dal while e scrivo
# # cosa succede se la mail è giusta 
# print("Giusto!")

#####################################################################

# # creo un programma che inizia chiedendomi un numero, lo somma a 0,
# # poi inizia a chiedermi numeri sommandoli al numero precedente 
# # continuamente fino a quando non scrivo stop

# # 1. definisco numero di partenza
# a = 0

# # 2. prima domanda all'utente
# numero = input("Dimmi un numero a caso: ")

# # finchè non scrivo stop somma i numeri
# while numero != "stop":
#     a = a + int(numero)
#     print(f"la somma dei tuoi numeri è {a}")
#     numero = input("dimmi un altro numero, altrimenti dimmi stop: ")

# print(f"Ti sei fermato a {a}")