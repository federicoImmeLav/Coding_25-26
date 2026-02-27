import turtle
import random

turtle.tracer(0)

# creo il personaggio
pg = turtle.Turtle()
pg.shape("square")
pg.color("green")
pg.penup() # cosi non disegna mentre si muove

# posiziono il personaggio in basso
pg.goto(0, -300) # in mezzo e y in basso

# creo la mela
mela = turtle.Turtle()
mela.shape("circle")
mela.color("red")
mela.penup()

# posiziono la mela nella sua posizione di partenza
mela.goto(0, 300)

# creo una turtle che scrive
punti = 0
penna = turtle.Turtle()
penna.penup()
penna.hideturtle() # nascono la turtle
penna.goto(0,320)
penna.write(f"Punteggio: {punti}", align = "center")

# creo la schermata di gioco
s = turtle.Screen()
# metto il gioco in ascolto
s.listen()

# creo dizionario dei tasti
tasti = {
    "a": False,
    "d": False
}

# funzioni che cambiano i tasti in True e False
def tasto_premuto(tasto):
    tasti[tasto] = True

def tasto_alzato(tasto):
    tasti[tasto] = False

# associo le funzioni ai tasti premuti e rilasciati
s.onkeypress(lambda: tasto_premuto("a"), "a")
s.onkeypress(lambda: tasto_premuto("d"), "d")

s.onkeyrelease(lambda: tasto_alzato("a"), "a")
s.onkeyrelease(lambda: tasto_alzato("d"), "d")

def movimento():
    # bisogna dire alla funzione che esiste una variabile
    # che si chiama punti
    global punti
    if tasti["a"]:
        pg.setheading(180)
        pg.forward(10)
    elif tasti["d"]:
        pg.setheading(0)
        pg.forward(10)

    # mela che cambia la y in giù ogni volta di 5
    mela.sety(mela.ycor() - 5)

    # se la mela è vicina al pg riparte da sopra perchè viene presa
    if pg.distance(mela) < 20:
        punti += 1 # aumenta punti di 1
        penna.clear()
        penna.write(f"Punteggio: {punti}", align = "center")
        mela.goto(random.randint(-200,200),300)

    # se la mela esce dalla schermata, ricomincia
    if mela.ycor() < -300:
        mela.goto(random.randint(-200,200),300)

    turtle.update() # aggiorno la schermata ogni volta che aggiorno il gioco
    s.ontimer(movimento, 10) # ripete la funzione ogni 10 ms

movimento()

# tiene aperta la schermata
s.mainloop()