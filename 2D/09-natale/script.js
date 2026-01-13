function leggi() {
    let nome = document.getElementById("nome").value;
    console.log(nome)
    document.getElementById("home").style.display = "none";
    document.getElementById("benvenuto").innerHTML ="ciao " + nome + " Buon Natale";
    document.getElementById("natale").style.display = "flex";
}

