import turtle
import random

turtle.tracer(0)
# creo la schermata
s = turtle.Screen()
s.listen()

# creo la forma
forma = turtle.Turtle()
forma.shape("circle")
forma.penup()
forma.hideturtle()

# scritta con le istruzioni
testo = turtle.Turtle()
testo.hideturtle()
testo.penup()
testo.goto(0, 250)
testo.write("Premi B, V, R a seconda del colore del cerchio", font=("Arial", 20), align="center")

# creo punteggio
punti = 0
punteggio = turtle.Turtle()
punteggio.hideturtle()
punteggio.penup()
punteggio.goto(0, -250)
punteggio.write(f"Punti: {punti}", font=("Arial", 20), align="center")

# variabile del colore
colore_forma = ""

ritardo = 1000

# creo la funz che fa comparire il cerchio di un colore casuale
def compari_cerchio():
    global colore_forma, ritardo
    # scelgo colore casuale
    colore_forma = random.choice(["green", "blue", "red"])
    # coordiate x e y a caso
    x = random.randint(-240, 240)
    y = random.randint(-240, 240)
    forma.goto(x,y)

    forma.color(colore_forma)
    forma.showturtle()

    turtle.update()
    s.ontimer(cambia_cerchio, ritardo)

# creo la funz che fa sparire il cerchio e lo fa ricomparire
def cambia_cerchio():
    forma.hideturtle()
    compari_cerchio()

# creo la funz che controlla che i tasti siano corrispondenti al colore
def controlla_colore(colore):
    global punti
    if colore == colore_forma:
        punti += 1
        punteggio.clear()
        punteggio.write(f"Punti: {punti}", font=("Arial", 20), align="center")

    elif colore != colore_forma:
        punti -= 1
        punteggio.clear()
        punteggio.write(f"Punti: {punti}", font=("Arial", 20), align="center")

# controllo il blu
s.onkey(lambda: controlla_colore("blue"), "b")
# controllo il rosso
s.onkey(lambda: controlla_colore("red"), "r")
# controllo il verde
s.onkey(lambda: controlla_colore("green"), "v")

# faccio partire la funzione compari_cerchio()
compari_cerchio()

# schermata aperta
s.mainloop()