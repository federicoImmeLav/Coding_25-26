import turtle
import random

# creo la schermata di gioco
schermo = turtle.Screen()
schermo.listen()

# creo la turtle a forma di triangolo 
barca = turtle.Turtle()
barca.shape("triangle") # forma triangolo
barca.color("brown") # cambio il colore
barca.penup()

# creo la turtle circolare per il pesce
pesce = turtle.Turtle()
pesce.shape("circle") # cerchio
pesce.color("orange")
pesce.penup()

# creo turtle che scrive il punteggio
punteggio = 0
display = turtle.Turtle()
display.hideturtle() # nascondo la turtle
display.teleport(0,280) # sposto la turtle in alto
display.write(f"{punteggio}", font=("Arial", 20), align="center")

# creo le coordinate casuali e ci metto il pesce
pesce.teleport(random.randint(-250,250), random.randint(-250,250))

# creo turtle del nemico
squalo = turtle.Turtle()
squalo.shape("square")
squalo.color("blue")
squalo.penup()
squalo.teleport(250,250)

# creo funzione vai_su()
def vai_su():
    # giro la barca verso l'alto
    barca.setheading(90)
    barca.forward(20)

def vai_giu():
    barca.setheading(-90)
    barca.forward(20)

def vai_destra():
    barca.setheading(0)
    barca.forward(20)

def vai_sinistra():
    barca.setheading(180)
    barca.forward(20)

# creo la funzione del gioco, cioè che continua all'infinito a 
# controllare che barca e pesce siano vicini e nel caso aggiorna
# il punteggio e fa altre cose
def movimento():
    global punteggio
    # controllo la posizione x e y di barca e pesce 
    # e vedo se sono vicini
    if barca.distance(pesce) < 20:
        pesce.teleport(random.randint(-250,250), random.randint(-250,250))
        punteggio += 1
        display.clear() # cancello la scritta
        display.write(f"{punteggio}", font=("Arial", 20), align="center")

    if squalo.xcor() > barca.xcor():
        squalo.setx(squalo.xcor() - 5)
    elif squalo.xcor() < barca.xcor():
        squalo.setx(squalo.xcor() + 5)

    if squalo.ycor() > barca.ycor():
        squalo.sety(squalo.ycor() - 5)
    elif squalo.ycor() < barca.ycor():
        squalo.sety(squalo.ycor() + 5)
    
    if squalo.distance(barca) < 20:
        display.clear()
        display.write("Hai perso!")
        barca.hideturtle()
        return

    # ripeto la funzione movimento all'infinito
    schermo.ontimer(movimento, 100)

# chiamo la funzione movimento
movimento()

# collego vai_su alla freccia su
schermo.onkeypress(vai_su, "Up")
schermo.onkeypress(vai_giu, "Down")
schermo.onkeypress(vai_destra, "Right")
schermo.onkeypress(vai_sinistra, "Left")

# tengo la schermata aperta
schermo.mainloop()