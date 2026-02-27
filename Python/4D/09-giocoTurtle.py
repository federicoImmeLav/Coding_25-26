import turtle
import random # importo la libreria a caso

# creo lo schermo in cui gioco 
s = turtle.Screen()
s.bgcolor("white") # colore di sfondo

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")


# creo le funzioni per i comandi delle frecce
def su():
    # la funzione deve girare verso su e poi andare avanti
    t.setheading(90) # giro di 90 gradi
    t.forward(30) # vado avanti di 30

def giu():
    t.setheading(270)
    t.forward(30)

def destra():
    t.setheading(0)
    t.forward(30)

def sinistra():
    t.setheading(180)
    t.forward(30)

# imposto che se schiaccio la barra spazio la turtle smette di disegnare
# se la rischiaccio ricomincia a disegnare
# Mi serve una variabile che sia associata al su e giù
turtle_giu = True

# creo la funzione che alza e abbassa la turtle
def cambia_turtle():
    global turtle_giu # imposto che la variabile venga usata fuori

    if turtle_giu:
        t.penup() # la turtle si alza
        turtle_giu = False
    else:
        t.pendown() # abbasso la turtle
        turtle_giu = True

# comando che cancella il disegno
def cancella():
    t.reset()
    t.color("blue")

# tasto per cambiare colore della turtle
def verde():
    t.color("green")

# funzione che cambia il colore a caso
def colore_casuale():
    colori = ["red", "pink", "purple", "green", "black"] # lista di colori
    # scelgo un colore a caso
    scelta = random.choice(colori)
    # uso il colore per la turtle
    t.color(scelta)

# aggiungo il comando che quando premo i tasti, attiva la funzione
# imposto python affinchè aspetti che io faccia qualcosa
s.listen()
s.onkey(su, "Up")
s.onkey(giu, "Down")
s.onkey(sinistra, "Left")
s.onkey(destra, "Right")
s.onkey(cambia_turtle, "space")
s.onkey(cancella, "c")
s.onkey(verde, "a")
s.onkey(colore_casuale, "r")


# mantengo la schermata aperta 
s.mainloop()

#########################################################################################

# creo una turtle che si muove a caso sia direzione che distanza

t = turtle.Turtle()
t.shape("turtle")

for i in range(30):
    t.forward(random.randint(10,60))
    t.setheading(random.randint(0,360))

turtle.done()
