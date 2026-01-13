# # stampo una stringa 
# print("Ciao")

# # metto una stringa in una variabile e la stampo 
# saluto = "buongiorno"
# print(saluto)

# # unisco in una unica frase una stringa e un numero 
# eta = 56
# nome = "Emanuele"
# print(f"{nome} dimostra {eta} anni")

# # posso anche dare io le informazioni con input
# luogo = input("Dove abiti? ")
# # se chiedo un numero metto int o float
# anni = int(input("In che anno sei nato? ")) 

##########################################################################################
# Creo un programma che mi chiede il nome, in che anno sono nato
# e il mese (lo indichiamo con il numero),
# il programma poi calcola l' età in base all'anno 
# se il mese in cui la persona è nata è già passato, è giusto
# se il mese in cui la persona è nata non è ancora passato, 
# aggiusta il calcolo

# indico al programma in che anno e mese siamo
# anno_corrente = 2026
# mese_corrente = 1

# # chiedo all'utente come si chiama, in che anno e mese è nato/a
# nome = input("Come ti chiami? ")
# anno_nascita = int(input("In che anno sei nato/a? "))
# mese_nascita = int(input("In che mese sei nato/a? (in numero) "))

# eta = anno_corrente - anno_nascita

# # indico se il mese è già passato ponendo la condizione per cui 
# # il mese di nascita è maggiore o minore del mese corrente 
# if mese_nascita < mese_corrente:
#     print(eta)
# else:
#     print(eta - 1)

#################################################################################
# Creo un programma che stampa i primi 50 numeri (for)
# se il numero è pari, di fianco al numero stampa (: pari) (if)
# se il numero è divisible per tre me lo dice (: divisible per tre)
# for i in range(50):
#     # metto un if dentro al for
#     if i % 2 == 0 and i % 3 == 0: # con and le condizioni valgono entrambe
#         print(f"{i}: è pari e divisibile per tre")
#     elif i % 2 == 0: # vuol dire se il numero è pari
#         print(f"{i}: è pari")
#     elif i % 3 == 0:
#         print(f"{i}: è divisibile per tre")
#     else: 
#         print(i)




