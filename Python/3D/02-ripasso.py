
# # #per salvare un numero bisogna mettere int davanti al comando
# # #anno = int(input("In che anno sei nato?"))

# # #eta = 2025 - anno
# # #print(eta)

# # nome = input("Come ti chiami?")
# # #comando per contare le lettere di una stringa è len()
# # #print(len(nome)) #in questo modo lo faccio una volta e lo stampo

# # #il comando per convertire un numero in una stringa è str()
# # lunghezza = len(nome) 
# # #print(nome + " è lungo " + str(lunghezza) + " caratteri")
# # #python inizia a contare dallo 0
# # #print(nome[0])
# # #per stampare più di una lettera della stringa si usano i :
# # #print(nome[2:5])

# frase = "In 3D non si riesce a fare lezione"
# print(len(frase))
# #comando per trasformare tutta la stringa in maiuscolo
# print(frase.upper())
# #print(frase.lower())
# #posso cambiare il contenuto di una stringa
# #print(frase.replace("3D", "2D"))
# #scoprire in che posizione è un carattere
# #print(frase.find("D"))

# nome = input("Come ti chiami?")
# #print di "Ciao [nome], il tuo nome è lungo [lunghezza], caratteri"
# #print di "La prima lettera del tuo nome è []"
# #print di "Il tuo nome tutto in maiuscolo è []"
# print("Ciao " + nome + ", il tuo nome è lungo " + str(len(nome)) + " caratteri")
# print("La prima lettera del tuo nome è " + nome[0])
# print("Il tuo nome tutto in maiuscolo è "+ nome.upper())


# password = input("Scegli una password di 9 caratteri")
# lunghezza = len(password) #salvo quanto è lunga la password
# #stiamo attenti all'indentazione
# if lunghezza > 9:
#     print("La tua password è troppo lunga")
# elif lunghezza < 9:
#     print("La tua password è troppo corta")
# elif lunghezza == 9:
#     print("La tua password va bene")

#ciclo for serve a far fare al nostro programma qualcosa finchè 
# non si verifica una determinata condizione
# for i in range(10):
#     print("ciao")

# for i in range(10):
#     print(i)

# nome = "Federico"
# for i in nome:
#     print(i)


#esempio con il while
# a = 0
# while a < 10:
#     print(a)
#     a = a + 1 #se non aggiorno la variabile il while va avanti all'infinito