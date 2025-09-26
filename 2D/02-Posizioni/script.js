
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