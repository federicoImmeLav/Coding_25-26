# Comando per stampare 
# print("ciao") 

# Per lavorare con i dati servono dei contenitori per 
# metterceli: variabili 
# nome = "Hossam" # le parole si chiamano stringhe
# print(nome)

# anni = 18 # i numeri si chiamano int o float
# print(anni)

# in python stringhe e numeri non si mischiano
# per unire numeri e stringhe si possono fare due cose
# la prima è trasformare i numeri in stringhe
# con il comando str 
# print("Ciao " + nome + " hai " + str(anni) + " anni")

# l'altro modo per unire stringhe e numeri è usare f 
# print(f"Ciao {nome} hai {anni} anni")

###########################################################################################
# Si può interagire con python, con print lui parla
# con noi, per parlare noi con lui si usa input 
# quando si fa input py salva tutto come stringhe

nome = input("Come ti chiami? ")

# quando chiedo un numero (anno), lo devo convertire in int
anno = int(input("Qual è il tuo anno di nascita? "))
# sottraggo l'anno inserito dall'anno in cui siamo
anni = 2026 - anno
print(f"Ciao {nome}! hai {anni} anni!")


