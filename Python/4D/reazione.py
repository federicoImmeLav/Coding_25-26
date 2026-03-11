import turtle
import random
import time

# --- SCHERMO ---
s = turtle.Screen()
s.setup(600, 400)
s.title("Test tempo di reazione")
s.listen()

# --- QUADRATO ROSSO ---
target = turtle.Turtle()
target.shape("square")
target.color("red")
target.penup()
target.hideturtle()

# --- TESTO ---
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 100)
pen.write("Premi SPAZIO per iniziare", align="center", font=("Arial", 16, "normal"))

# --- VARIABILI ---
stato = "attesa"   # attesa, preparazione, reazione
tempo_inizio = 0

# --- FUNZIONE CHE MOSTRA IL QUADRATO ---
def mostra_quadrato():
    global stato, tempo_inizio
    target.showturtle()
    tempo_inizio = time.perf_counter()
    stato = "reazione"

# --- PRESSIONE DELLA BARRA SPAZIATRICE ---
def spazio():
    global stato

    # prima pressione: avvia il test
    if stato == "attesa":
        pen.clear()
        pen.write("Aspetta il quadrato rosso...", align="center", font=("Arial", 16, "normal"))
        
        ritardo = random.randint(0, 5000)  # millisecondi
        s.ontimer(mostra_quadrato, ritardo)
        
        stato = "preparazione"

    # seconda pressione: misura il tempo
    elif stato == "reazione":
        tempo_fine = time.perf_counter()
        reazione = (tempo_fine - tempo_inizio) * 1000

        target.hideturtle()
        pen.clear()
        pen.write(f"Tempo di reazione: {int(reazione)} ms\nPremi spazio per riprovare",
                  align="center", font=("Arial", 16, "normal"))

        stato = "attesa"

# --- TASTO SPAZIO ---
s.onkey(spazio, "space")

s.mainloop()