# creo un programma che mi chiede che ore sono,
# se l'ora è più grande delle 12, mi dice buon pomeriggio
# se l'ora è minore delle 12, mi dice buongiorno
# se l'ore è maggiore di 18 mi dice buonasera

# codice che mi chiede le ore
# ore = int(input("Che ore sono? (senza minuti) "))
# print(ore) # controllo che salva la cosa giusta

# if ore > 18:
#     print("Buonasera")
# elif ore <= 12:
#     print("Buongiorno")
# elif ore > 12:
#     print("Buon pomeriggio")
# con gli if devo sempe andare dal più grande al più piccolo 
# altrimenti il programma si ferma prima 
####################################################################################
# programma che mi chiede anno e mese di nascita e mi dice quanti anni ho

# definisco in che anno siamo
anno_corrente = 2026
mese_corrente = 5

# chiedo le informazioni all'utente 
anno_nascita = int(input("In che anno sei nato/a? "))
mese_nascita = int(input("In che mese sei nato/a? (1-12) "))

# calcolo l'età in base agli anni, senza considerare il mese
anni = anno_corrente - anno_nascita

# in base al mese in cui siamo, rispetto a quello di nascita 
# sottraggo un anno se il mese di nascita è maggiore del mese corrente 
if mese_nascita > mese_corrente:
    anni = anni - 1

print(f"Hai {anni} anni")