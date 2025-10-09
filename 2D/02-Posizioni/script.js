
// creo la funzione per leggere i numeri 
function numeri() {
    // tutto quello che scrivo qui sarà quello che
    // la funzione deve fare 
    let giorni = parseFloat(document.getElementById("giorni").value);
    // prendo il numero che c'è in input e lo metto nella variabile 

    console.log(giorni);
    // carico la variabile nella console 
    if(giorni < 20) {
        document.getElementById("cerchio").style.backgroundColor = "green";
    }
    else if (giorni < 35) {
        document.getElementById("cerchio").style.backgroundColor = "orange";
    }
    else if (giorni > 36) {
        document.getElementById("cerchio").style.backgroundColor = "red";
    }
    else {
        document.getElementById("cerchio").style.backgroundColor = "gray";
    }
}


// creo una variabile che è la mia prima materia 
let materia1 = "MATEMATICA";
// faccio il comando che scrive matematica dentro al h3 materia1 
document.getElementById("materia1").textContent = materia1;

// creo la variabile di voto1 
let voto1 = 70;
document.getElementById("voto1").textContent = voto1;

// imposto che se il numero è maggiore di 60 si scrive in verde 
if(voto1 > 60) {
    document.getElementById("voto1").style.color = "green";
}
 
// creo una variabile che tiene dentro più elementi 
let materie = ["ITALIANO", "CODING", "INGLESE","GINNASTICA", "RELIGIONE"];

// creo i voti 
let voti = [60, 35, 70, 90, 100];

console.log(materie);

console.log(materie[0]);
console.log(materie[3]);

// creo le funzioni che scrivono le materie prendendole da array 
document.getElementById("materia2").textContent = materie[0];
document.getElementById("materia3").textContent = materie[1];
document.getElementById("materia4").textContent = materie[2];
document.getElementById("materia5").textContent = materie[3];
document.getElementById("materia6").textContent = materie[4];

// metto i voti nei rispetti div 
document.getElementById("voto2").textContent = voti[0];
document.getElementById("voto3").textContent = voti[1];
document.getElementById("voto4").textContent = voti[2];
document.getElementById("voto5").textContent = voti[3];
document.getElementById("voto6").textContent = voti[4];

// controllo che ciascun voto sia maggiore o minore di 60 e gli cambio il colore 
if(voti[0] > 59) {
    document.getElementById("voto2").style.color = "green"
}
if(voti[1] > 59) {
    document.getElementById("voto3").style.color = "green"
}
if(voti[2] > 59) {
    document.getElementById("voto4").style.color = "green"
}
if(voti[3] > 59) {
    document.getElementById("voto5").style.color = "green"
}
if(voti[4] > 59) {
    document.getElementById("voto6").style.color = "green"
}






