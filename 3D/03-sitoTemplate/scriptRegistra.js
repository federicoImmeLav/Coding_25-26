function password() {
    let user = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    console.log(user + password);

    // creo un oggetto con le info dell'utente 
    let utente = {
        nome: user,
        password: password
    }
    console.log(utente)
}

let admin = [
    {nome:"Riccardo", cognome:"Bozian",classe: "2D"},
    {nome:"Enrico", cognome:"Righi", classe:"4D"},
    {nome: "Federico", cognome:"Pozzi",classe:"2A"}
] 

function inserisci1(){
    document.getElementById("inserisci").innerHTML = admin[0].cognome;
}
function inserisci2(){
    document.getElementById("inserisci").innerHTML = admin[1].cognome;
}
function inserisci3(){
    document.getElementById("inserisci").innerHTML = admin[2].cognome;
}

let Francesco = [
    {materia: "Coding", voto: "0"},
    {materia: "Matematica", voto: "10"},
    {materia: "Inglese", voto: "0"},
    {materia: "IRC", voto: "90"},
    {materia: "Italiano", voto: "40"},
]

  function mostraVoti(arrayUtente) {
    const contenitore = document.getElementById("contenitore");

    // Pulisco il contenitore prima di aggiungere nuovi div
    contenitore.innerHTML = "";

    arrayUtente.forEach(item => {
      const div = document.createElement("div");
      div.className = "votoDiv";

      const p = document.createElement("p");
      p.textContent = `${item.materia}: ${item.voto}`;

      div.appendChild(p);
      contenitore.appendChild(div);
    });
  }

  // Chiamo la funzione per mostrare i voti
  mostraVoti(Francesco);