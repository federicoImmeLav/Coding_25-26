import turtle
import random

# --- SCHERMO ---
s = turtle.Screen()
s.setup(600, 600)
s.title("Prendi le mele")
s.tracer(0)
s.listen()

# --- PERSONAGGIO (in basso) ---
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(0, -250)

# --- MELA ---
mela = turtle.Turtle()
mela.shape("circle")
mela.color("red")
mela.penup()
mela.goto(random.randint(-280, 280), 250)

# --- PUNTEGGIO ---
punteggio = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write(f"Punteggio: {punteggio}", align="center", font=("Arial", 16, "normal"))

# --- TASTI (solo destra e sinistra) ---
tasti = {"a": False, "d": False}

def tasto_premuto(tasto):
    tasti[tasto] = True

def tasto_alzato(tasto):
    tasti[tasto] = False

for k in tasti:
    s.onkeypress(lambda k=k: tasto_premuto(k), k)
    s.onkeyrelease(lambda k=k: tasto_alzato(k), k)

# --- MOVIMENTO ---
def movimento():
    global punteggio

    # movimento player
    if tasti["a"]:
        player.setx(player.xcor() - 20)
    elif tasti["d"]:
        player.setx(player.xcor() + 20)

    # mela cade verso il basso
    mela.sety(mela.ycor() - 10)

    # se prende la mela
    if player.distance(mela) < 30:
        punteggio += 1
        pen.clear()
        pen.write(f"Punteggio: {punteggio}", align="center", font=("Arial", 16, "normal"))
        mela.goto(random.randint(-280, 280), 250)

    # se la mela arriva in fondo
    if mela.ycor() < -280:
        mela.goto(random.randint(-280, 280), 250)

    s.update()
    s.ontimer(movimento, 100)

movimento()
s.mainloop()