import turtle
import random

turtle.tracer(0)

# creo personaggio
pg = turtle.Turtle()
pg.shape("triangle")
pg.color("green")
pg.penup()

# creo turtle per i bordi
bordi = turtle.Turtle()
bordi.penup()
bordi.goto(300,300)
# disegno quadrato di 600 di lato
bordi.pendown()
bordi.pensize(5)
bordi.color("blue")
bordi.hideturtle()
for i in range(4):
    bordi.right(90)
    bordi.forward(600)

# creo la mela
mela = turtle.Turtle()
mela.penup()
mela.shape("circle")
mela.color("red")
mela.goto(0,150)

# creo il punteggio
punti = 0
punteggio = turtle.Turtle()
punteggio.penup()
punteggio.hideturtle()
punteggio.goto(0,310)
punteggio.write(f"Punti: {punti}", align="center")

# creo schermata di gioco
s = turtle.Screen()

# creo dizionario comandi
tasti = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}

# funzioni che cambiano i tasti da true a false e viceversa
def tasto_premuto(tasto):
    tasti[tasto] = True

def tasto_alzato(tasto):
    tasti[tasto] = False

s.listen() # metto il programma in ascolto

# associo le funzioni
s.onkeypress(lambda: tasto_premuto("w"), "w")
s.onkeypress(lambda: tasto_premuto("a"), "a")
s.onkeypress(lambda: tasto_premuto("s"), "s")
s.onkeypress(lambda: tasto_premuto("d"), "d")

s.onkeyrelease(lambda: tasto_alzato("w"), "w")
s.onkeyrelease(lambda: tasto_alzato("a"), "a")
s.onkeyrelease(lambda: tasto_alzato("s"), "s")
s.onkeyrelease(lambda: tasto_alzato("d"), "d")

# creo la funz gioco()
def gioco():
    global punti # inserisco nella funzione la variabile
    # if dei tasti
    if tasti["w"]:
        pg.setheading(90) # punta su
        pg.forward(10) # muovi avanti di 10
    elif tasti["s"]:
        pg.setheading(-90)
        pg.forward(10)
    elif tasti["a"]:
        pg.setheading(180)
        pg.forward(10)
    elif tasti["d"]:
        pg.setheading(0)
        pg.forward(10)

    # if che controlla i bordi
    if pg.xcor() > 290:
        pg.setx(290)
    elif pg.xcor() < -290:
        pg.setx(-290)
    if pg.ycor() > 290:
        pg.sety(290)
    elif pg.ycor() < -290:
        pg.sety(-290)
    
    # contatto tra mela e pg
    if pg.distance(mela) < 20:
        # numero a caso tra -280 e 280
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        mela.goto(x,y)
        # aggiorno il punteggio
        punti += 1
        punteggio.clear()
        punteggio.write(f"Punti: {punti}", align="center")

    turtle.update()
    s.ontimer(gioco, 10)

gioco()
# tengo la schermata aperta
s.mainloop()

# ORDINE DI LAVORO PER VIDEOGIOCO
# 1. Creo personaggio e schermata di gioco
# 2. Creo dizionario dei comandi e funzioni per i tasti
# 3. Associo le funzioni all'azione di premere e mollare i tasti
# 4. Creo la funzione di gioco
# 5. Creo e faccio turtle dei bordi
# 6. If che controlla che non supero i bordi
# 7. Creo turtle della mela
# 8. Funzione che se prendo la mela, la mela scappa
# 9. Punteggio quando prendo la mela