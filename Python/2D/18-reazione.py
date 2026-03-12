import turtle
import time
import random

# creo la schermata di gioco
s = turtle.Screen()

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

# creo la funz che mostra il semaforo e che inizia a contare 
# il tempo che passa
def mostra_semaforo():
    # faccio comparire il semaforo
    semaforo.showturtle()
    

s.mainloop()