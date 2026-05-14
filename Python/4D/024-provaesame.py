# Macchinina che deve prendere la benzina
# benzina che cambia posto a caso ogni volta che la prendo
# timer di 7 secondi che ogni volta che prendo la benzina
# si resetta
# gomme che se le prendiamo facciamo un 1 

# con turtle
# random
# time / schermo.ontimer()

# 1. Macchina che si muove con le frecce
# 2. Benzina casuale che interagisce con la macchina
# 3. Funzione del gioco
# 4. Timer che scrive i secondi rimanenti a schermo
# 5. Funzione che aggiorna ogni secondo
# 6. Aggiungo una turtle che rappresenta le gomme
# 7. Aggiungo una turtle per il punteggio
# 8. Se la macchina prende la gomma faccio 1 punto e la gomma si sposta



import turtle
import random

s = turtle.Screen()
s.listen()

macchina = turtle.Turtle()
macchina.shape("triangle")
macchina.color("red")
macchina.penup()

benzina = turtle.Turtle()
benzina.shape("circle")
benzina.color("orange")
benzina.penup()
benzina.teleport(random.randint(-250,250), random.randint(-250,250))

secondi = 7
tempo = turtle.Turtle()
tempo.teleport(-300,300)
tempo.hideturtle()
tempo.write(f"Tempo rimanente: {secondi}")

# funzione che fa girare e andare avanti
def vai_destra():
    macchina.setheading(0)
    macchina.forward(20)

def vai_sinistra():
    macchina.setheading(180)
    macchina.forward(20)

def vai_su():
    macchina.setheading(90)
    macchina.forward(20)

def vai_giu():
    macchina.setheading(-90)
    macchina.forward(20)

def gioco():
    global secondi
    if macchina.distance(benzina) < 20:
        benzina.teleport(random.randint(-250,250), random.randint(-250,250))
        secondi = secondi + 8

    s.ontimer(gioco, 100)

# creo funzione che fa scendere il tempo
def cronometro():
    global secondi
    if secondi > 0: 
        secondi -= 1
        tempo.clear()
        tempo.write(f"Tempo rimanente: {secondi}")
    if secondi == 0:
        macchina.hideturtle()
    s.ontimer(cronometro, 1000)

cronometro()
gioco()

# comando per i tasti
s.onkey(vai_destra, "Right")
s.onkey(vai_sinistra, "Left")
s.onkey(vai_su, "Up")
s.onkey(vai_giu, "Down")

s.mainloop()
