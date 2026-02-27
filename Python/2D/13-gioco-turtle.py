import turtle
import random # portare le cose a caso

# creo la turtle
t = turtle.Turtle()
t.shape("turtle")

# creo la schermata di gioco
s = turtle.Screen()

# creare i comandi per le frecce per muovere la turtle
# creare funzioni di movimento
def su():
    t.setheading(90) # punto la turtle in direzione verticale
    t.forward(50)

def giu():
    t.setheading(270)
    t.forward(50)

def destra():
    t.setheading(0)
    t.forward(50)

def sinistra():
    t.setheading(180)
    t.forward(50)

# funzione per colore casuale
def colore_casuale():
    # creo una lista di colori
    colori = ["red", "blue", "black", "purple", "green"]
    t.color(random.choice(colori)) # scelgo a caso un elemento della lista

# creo la funzione che cancella tutto
def cancella():
    t.reset() #cancella tutto e riporta la turtle in mezzo

# devo associare le funzioni di movimento 
# ai tasti richiesti
s.listen() # py aspetta che faccio qualcosa

# comando per far si che quando schiaccio il 
# tasto si accende la funzione
s.onkey(su,"Up")
s.onkey(giu, "Down")
s.onkey(destra, "Right")
s.onkey(sinistra, "Left")
s.onkey(cancella, "space")
s.onkey(colore_casuale, "a")

# comando che tiene la schermata aperta
s.mainloop()