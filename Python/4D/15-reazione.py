import turtle
import random
import time

# creo la schermata di gioco
s = turtle.Screen()
s.listen()

# creo il semaforo
semaforo = turtle.Turtle()
semaforo.color("red")
semaforo.shape("circle")
semaforo.shapesize(5)
semaforo.hideturtle()

# creo turtle del testo
testo = turtle.Turtle()
testo.hideturtle()
testo.penup()
testo.goto(0,200)
testo.write("Premi SPAZIO per iniziare", font=("Arial", 20), align="center")

# creo le variabili necessarie
tempo_inizio = 0
# creo la variabile dei momenti del gioco
stato = "attesa"

# creo il blocco del semaforo che compare
# deve comparire il semaforo + devo iniziare a contare il tempo che passa
# lo stato deve cambiare
def mostra_semaforo():
    global tempo_inizio, stato # dico alla funzione che var usare
    semaforo.showturtle() # mostro il semaforo
    tempo_inizio = time.time() # inizio a contare il tempo
    stato = "semaforo" # cambio lo stato in cui sono

# funzione del gioco
# 1: aspetta che premo la prima volta spazio
# 2: quando premo spazio fa partire la funz mostra_semaforo()
# 3: aspetta che premo ancora spazio
# 4: quando premo spazio conta quanto tempo è passato da quando 
# è comparso il semaforo 
# 5: mi dice quanto tempo ci ho messo
# 6: riparte tutto

def gioco():
    global stato
    print("barra premuta") # controllo che funz va con barra spaz
    if stato == "attesa":
        testo.clear()
        testo.write(f"Aspetta il semaforo...", align="center", font=("Arial", 20))
        ritardo = random.randint(1000,5000) # momento a caso tra 1 e 5s
        s.ontimer(mostra_semaforo,ritardo)

    elif stato == "semaforo":
        tempo_fine = time.time()
        tempo_reaz = (tempo_fine - tempo_inizio) * 1000 # calcolo tempo effettivo

        semaforo.hideturtle()
        testo.clear()
        testo.write(f"Tempo di reazione: {int(tempo_reaz)} ms", font=("Arial", 20), align="center")
        # rimetto stato di attesa
        stato = "attesa"

s.onkey(gioco, "space")

s.mainloop()