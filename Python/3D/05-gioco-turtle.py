import turtle
import time 
import random

# creo la schermata
schermo = turtle.Screen()
schermo.listen() 

# creo la turtle che scrive
testo = turtle.Turtle()
# sposto la turtle in alto
testo.teleport(0, 200)
testo.write("Premi SPAZIO per iniziare", font=("Arial",20), align="center")
# nascondo la turtle
testo.hideturtle()

# creo turtle per il cerchio rosso
semaforo = turtle.Turtle()
semaforo.shape("circle")
semaforo.shapesize(5)
semaforo.color("red")
# cerchio non si vede all'inizio
semaforo.hideturtle()

# creo la variabile che traccia i momenti di gioco
momento = "spento"
tempo_inizio = 0

# creo la funzione per far apparire il cerchio
def appari():
    testo.clear()
    testo.write("Aspetta il semaforo...", font=("Arial",20), align="center")
    n = random.randint(1, 5)
    time.sleep(n)
    semaforo.showturtle()

# creo la funzione del gioco
def gioco():
    # diciamo alla funz di usare una variabile fuori
    global momento, tempo_inizio
    if momento == "spento":
        appari()
        tempo_inizio = time.time()
        momento = "acceso"
    elif momento == "acceso":
        semaforo.hideturtle()
        tempo_fine = time.time()
        reazione = (tempo_fine - tempo_inizio) * 1000
        testo.clear()
        testo.write(f"Tempo: {int(reazione)} ms", font=("Arial",20), align="center")
        momento = "spento"

# quando premo spazio si accende la funzione appari()
schermo.onkey(gioco, "space")

# tengo la schermata aperta
schermo.mainloop()