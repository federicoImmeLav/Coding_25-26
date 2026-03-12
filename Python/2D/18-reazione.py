import turtle
import time
import random

# creo la schermata di gioco
s = turtle.Screen()
s.listen()

# creo la turtle della scritta
testo = turtle.Turtle()
testo.penup()
testo.hideturtle()
testo.goto(0,150)
testo.write(f"Premi SPAZIO per iniziare", font=("Arial", 20), align="center")

# creo la turtle del semaforo
semaforo = turtle.Turtle()
semaforo.shape("circle")
semaforo.shapesize(5)
semaforo.color("red")
semaforo.hideturtle() # nascondo la turtle all'inizio

# variabile che tiene traccia del gioco
stato = "attesa"
tempo_inizio = 0

# creo la funz che mostra il semaforo e che inizia a contare 
# il tempo che passa
def mostra_semaforo():
    global stato, tempo_inizio
    # salvo il tempo in cui mostro il semaforo
    tempo_inizio = time.time()
    semaforo.showturtle()
    # cambio lo stato del gioco
    stato = "semaforo"

# creo funzione del gioco
def gioco():
    global stato
    # se lo stato è in attesa, mostro il semaforo
    if stato == "attesa":
        # scritta che mi dice di aspettare il semaforo
        testo.clear()
        testo.write("Aspetta il semaforo...", font=("Arial", 20), align="center")
        ritardo = random.randint(1000,5000) # numero a caso tra 1 e 5 secondi
        s.ontimer(mostra_semaforo, ritardo)

    elif stato == "semaforo":
        # salvo un altro valore di tempo e calcolo 
        # quanto è passato da tempo_inizio
        tempo_fine = time.time()
        tempo_reaz = (tempo_fine - tempo_inizio) * 1000
        semaforo.hideturtle()
        testo.clear()
        testo.write(f"Reazione: {int(tempo_reaz)} ms", font=("Arial", 20), align="center")
        stato = "attesa"
        
s.onkey(gioco, "space") # accendi la funz se premo spazio
s.mainloop()