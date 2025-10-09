// creo la lista di persone che possono accedere al sito 
let nome = "Federico";
let amministratori = ["Federico", "Francesco", "Enrico", "Nipuna"]

function controllo() {
  let username =  document.getElementById("nome").value;
  console.log(username);
  if (amministratori.includes(username)) {
    console.log("Accesso consentito");
    // comando che apre una nuova pagina web 
    window.location.href = "home.html"
  }
  else {
    console.log("Ritenta")
    alert("ERRORE!!")
  }
}

