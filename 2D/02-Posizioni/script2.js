// creo un array con i giorni della settimana 
let giorni = ["lunedì", "martedì", "mercoledì","giovedì","venerdì"];

// scrivo dentro a il div che si chiama test l'elemento che sta al posto 2 dell'array 
document.getElementById("test").textContent = giorni[2];

// creo la funzione che va a leggere quello scrivo negli input 
// e crea un array con gli ingredienti
function creoLista() {
    // leggo il primo input 
    let i1 = document.getElementById("ingrediente1").value;
    console.log(i1);
    let i2 = document.getElementById("ingrediente2").value;
    console.log(i2);
    let i3 = document.getElementById("ingrediente3").value;
    console.log(i3);
}