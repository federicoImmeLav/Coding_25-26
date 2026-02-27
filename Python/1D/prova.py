import turtle
import random

# --- SCHERMO ---
s = turtle.Screen()
s.setup(600, 600)
s.title("Snake semplice")
s.tracer(0)  # disabilita aggiornamento automatico
s.listen()

# --- TESTA ---
testa = turtle.Turtle()
testa.shape("square")
testa.color("green")
testa.penup()

# --- CIBO ---
cibo = turtle.Turtle()
cibo.shape("circle")
cibo.color("red")
cibo.penup()
cibo.goto(0, 100)

# --- CORPO ---
corpo = []

# --- TASTI ---
tasti = {"w": False, "a": False, "s": False, "d": False}

def tasto_premuto(tasto):
    tasti[tasto] = True

def tasto_alzato(tasto):
    tasti[tasto] = False

for k in tasti:
    s.onkeypress(lambda k=k: tasto_premuto(k), k)
    s.onkeyrelease(lambda k=k: tasto_alzato(k), k)

# --- MOVIMENTO ---
def movimento():
    # muove la testa
    if tasti["w"]:
        testa.setheading(90)
        testa.forward(20)
    elif tasti["s"]:
        testa.setheading(-90)
        testa.forward(20)
    elif tasti["a"]:
        testa.setheading(180)
        testa.forward(20)
    elif tasti["d"]:
        testa.setheading(0)
        testa.forward(20)

    # controlla se la testa tocca il cibo
    if testa.distance(cibo) < 20:
        cibo.goto(random.randint(-280, 280), random.randint(-280, 280))
        segmento = turtle.Turtle()
        segmento.shape("square")
        segmento.color("dark green")
        segmento.penup()
        corpo.append(segmento)

    # muove il corpo (ogni segmento segue quello davanti)
    for i in range(len(corpo)-1, 0, -1):
        corpo[i].goto(corpo[i-1].xcor(), corpo[i-1].ycor())
    if corpo:
        corpo[0].goto(testa.xcor(), testa.ycor())

    # **aggiorna lo schermo**
    s.update()

    # richiama il movimento dopo 100ms
    s.ontimer(movimento, 100)

# --- AVVIA IL GIOCO ---
movimento()
s.mainloop()