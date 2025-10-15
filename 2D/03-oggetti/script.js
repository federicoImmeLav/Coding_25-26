// creo una variabile che è una scritta 
let nome = "Federico";
// scrivo la variabile dentro all'elemento che si chiama inserisci 
//document.getElementById("inserisci").innerHTML = nome;

// le variabili sono anche dei numeri 
let anno = 2025;
// con i numeri si possono fare le operazioni matematiche 
//document.getElementById("inserisci2").innerHTML = anno * 2;


// se voglio fare una lista mi conviene fare un array 
let spesa = ["pane", "acqua", "carne", "carote", "coca cola"];
// array conta gli elementi da 0 
// scrivo carne in inserisci3, devo riferirmi al 
// terzo elemento dell'array, ovvero quello in posizione
// numero 2
//document.getElementById("inserisci3").innerHTML = spesa[2];

let nome1 = "Alfonso";
let cognome1 = "Saponaro";
let eta1 = "2010";
let professione = "Ingegnere";

// creo una variabile che contiene tutte le caratteristiche,
// questa variabile si chiama oggetto 
let Vladut = {
    nome: "Vladut",
    cognome: "Enache",
    eta: "2008",
    professione: "sollevatore di polemiche"
}
// come chiamo gli elementi singoli dell'oggetto? 
//document.getElementById("inserisci4").innerHTML = Vladut.professione;


let amministratore = {
    username: "admin",
    password: "saponaro",
}

function accedi() {
    let user = document.getElementById("username").value;
    console.log(user);
    let pass = document.getElementById("password").value;
    console.log(pass);
    if(user == amministratore.username && pass == amministratore.password) {
        alert("benvenuto");
    }
    else {
        alert("errore!");
    }
}

