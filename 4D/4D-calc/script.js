function tasto(numero) {
    let a = document.getElementById("numeri");
    console.log(a);
    a.innerText = a.innerText + numero;
}

function cancella() {
    document.getElementById("numeri").innerText = "";
}

let primoNum = 0;
function somma() {
    // trasformo il primo numero in numero e lo salvo 
    primoNum = Number(document.getElementById("numeri").innerText);
    console.log(primoNum);
    document.getElementById("numeri").innerText = "";
}

function uguale() {
    let secondoNum = Number(document.getElementById("numeri").innerText);
    let risultato = primoNum + secondoNum;
    document.getElementById("numeri").innerText = risultato;
}