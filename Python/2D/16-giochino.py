import turtle
import random # comando per cose casuali
import time # importo i comandi per il tempo

turtle.tracer(0)

# creo personaggio
pg = turtle.Turtle()
pg.shape("square")
pg.color("green")
pg.penup()

# creo la mela
mela = turtle.Turtle()
mela.shape("circle")
mela.color("red")
mela.penup()
# posiziono la mela in un punto preciso di spawn
mela.goto(0,200)

# disegno con una turtle apposta il bordo di gioco
bordo = turtle.Turtle()
bordo.penup()
bordo.goto(0,300)
# inizio a disegnare il bordo
# personalizzo il bordo
bordo.color("blue")
bordo.pensize(5)

bordo.pendown()
bordo.goto(300,300)
bordo.goto(300,-300)
bordo.goto(-300,-300)
bordo.goto(-300,300)
bordo.goto(0,300)
# nascondo la turtle
bordo.hideturtle()

# creo la turtle che scrive i punti
punti = 0 # creo la variabile dei punti
punteggio = turtle.Turtle()
punteggio.penup()
punteggio.goto(0,315)
punteggio.hideturtle()
punteggio.write(f"Punteggio: {punti}", align = "center")

# turtle che scrive il tempo
tempo_passato = 0
tempo = turtle.Turtle()
tempo.penup()
tempo.goto(0,-320)
tempo.hideturtle()
tempo.write(f"Tempo rimasto: {tempo_passato}", align = "center")

# creo la schermata
s = turtle.Screen()

# salvo il momento in cui inizia il gioco
tempo_inizio = time.time()
# decido il tempo massimo di gioco
tempo_max = 30

# creo il dizionario dei comandi
comandi = {
    "a": False,
    "s": False,
    "d": False,
    "w": False
}

# creo le funzioni che cambiano i tasti da true a false e viceversa
def tasto_premuto(tasto):
    comandi[tasto] = True

def tasto_alzato(tasto):
    comandi[tasto] = False

s.listen() 
# finchè tengo premuto il tasto diventa True
s.onkeypress(lambda: tasto_premuto("w"), "w")
s.onkeypress(lambda: tasto_premuto("a"), "a")
s.onkeypress(lambda: tasto_premuto("s"), "s")
s.onkeypress(lambda: tasto_premuto("d"), "d")

# quando rilascio il tasto torna False
s.onkeyrelease(lambda: tasto_alzato("w"), "w")
s.onkeyrelease(lambda: tasto_alzato("a"), "a")
s.onkeyrelease(lambda: tasto_alzato("s"), "s")
s.onkeyrelease(lambda: tasto_alzato("d"), "d")

# creo la funzione del gioco, nella quale metto 
# tutti i comandi e le azioni
def gioco(): 
    # indico alla funzioni di usare la variabile punti
    global punti

    # controllo quanto tempo è passato all'inizio
    tempo_passato = time.time() - tempo_inizio
    # riscrivo ogni volta il tempo che passa
    tempo.clear()
    tempo.write(f"Tempo rimasto: {int(tempo_max - tempo_passato)}", align = "center")

    # se il tempo passato supera il tempo massimo, il gioco finisce
    if tempo_passato > tempo_max: 
        pg.hideturtle()
        mela.hideturtle()
        # faccio sparire tutto
        punteggio.clear()
        punteggio.goto(0,0)
        punteggio.write(f"Punteggio: {punti}", align = "center")

        turtle.update()
        return
        
    if comandi["w"]: 
        pg.setheading(90)
        pg.forward(10)
    elif comandi["s"]:
        pg.setheading(-90)
        pg.forward(10)
    elif comandi["a"]:
        pg.setheading(180)
        pg.forward(10) 
    elif comandi["d"]:
        pg.setheading(0)
        pg.forward(10)   
    
    # aggiungo la collisione con la mela
    if pg.distance(mela) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        mela.goto(x,y)
        punti += 1 # aumento punti di 1
        # cancello il punteggio di prima
        punteggio.clear()
        # riscrivo il nuovo punteggio
        punteggio.write(f"Punteggio: {punti}", align = "center")
    
    # condizioni per cui non posso uscire dal bordo,
    # devo controllare la x e la y del personaggio e evitare
    # che superi certi valori
    # per sapere x e y in qualunque momento si usa
    # .xcor() e .ycor()
    if pg.xcor() > 290:
        # riporto la x indietro
        pg.setx(290)
    elif pg.xcor() < -290:
        pg.setx(-290)
    
    if pg.ycor() > 290:
        pg.sety(290)
    
    elif pg.ycor() < -290:
        pg.sety(-290)

    turtle.update()
    # metto la funzione gioco in loop
    s.ontimer(gioco, 10)

# chiamo la funzione
gioco()
# tengo la schermata aperta
s.mainloop()
