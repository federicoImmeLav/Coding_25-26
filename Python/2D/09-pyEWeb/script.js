// Funzione che va a leggersi il json e inserisce
// al posto giusto le informazioni che prende 
fetch("studente.json") // va a prendersi il file che si chiama studente.json
.then(response => response.json()) // leggiti il json
// dopo che hai letto, prendi i dati e mettili nei punti indicati
.then(dati => {
    document.getElementById("nome").innerText = dati.nome;
    document.getElementById("eta").innerText = dati.eta;
    console.log(dati)
}
)