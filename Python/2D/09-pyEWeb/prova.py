# creo una funzione che costruisce un 
# elemento per poi andare in js, una sorta 
# di oggetto 

# def crea la funzione, poi si mette il nome della
# funzione, nelle parentesi gli elementi di cui ha bisogno 
def creo_info(nome, eta):
    return {
        "nome": nome,
        "eta": eta
    }

# dopo aver creato lo studente, devo costruire un file
# che possa essere preso da js e usato nella pagina web 
# devo creare un file che si chiama json

# importare dentro al file di python delle 
# funzioni aggiuntive che riguardano i file json
import json 

studente = creo_info("Emanuele", 16)

# crea il file json e scrivici dentro le info di studente
with open("studente.json", "w") as file:
    json.dump(studente, file)



