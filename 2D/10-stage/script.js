tot_ore = 304
max_assenze = 304/4

function calcola() {
    ore_fatte = parseFloat(document.getElementById("presenze").value);
    barra = ore_fatte * 100 / tot_ore;
    console.log(barra);
    barra1 = document.querySelector(".totale-pieno")
    barra1.style.width = barra + "%";

    ore_assenza = parseFloat(document.getElementById("assenze").value);
    barra2 = ore_assenza * 100 / max_assenze;
    barra3 = document.querySelector(".totale-pieno2")
    barra3.style.width = barra2 + "%";
}

