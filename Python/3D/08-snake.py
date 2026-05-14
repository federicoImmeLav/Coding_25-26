import turtle

turtle.tracer(0)

schermo = turtle.Screen()
schermo.listen()

# creo la turtle che disegna il bordo
quad = turtle.Turtle()
quad.color("purple")
quad.pensize(3)
quad.teleport(300,300)
quad.goto(300,-300)
quad.goto(-300,-300)
quad.goto(-300,300)
quad.goto(300,300)
quad.hideturtle()

# creo il personaggio
personaggio = turtle.Turtle()
personaggio.color("green")
personaggio.shapesize(2)
personaggio.penup()

# creo un dizionario di tasti
tasti = {
    "w": False,
    "a": False,
    "s": False,
    "d": False,
}

# creo la funzione che che cambia da False a True i valori
def tasto_premuto(tasto):
    tasti[tasto] = True

# funzione che fa diventare da True a False
def tasto_alzato(tasto):
    tasti[tasto] = False

# comando che fino a quando tengo premuto un tasto, attiva
# la funzione tasto_premuto che cambia il tasto da False a True
schermo.onkeypress(lambda: tasto_premuto("w"), "w")
schermo.onkeypress(lambda: tasto_premuto("a"), "a")
schermo.onkeypress(lambda: tasto_premuto("s"), "s")
schermo.onkeypress(lambda: tasto_premuto("d"), "d")

schermo.onkeyrelease(lambda: tasto_alzato("w"), "w")
schermo.onkeyrelease(lambda: tasto_alzato("a"), "a")
schermo.onkeyrelease(lambda: tasto_alzato("s"), "s")
schermo.onkeyrelease(lambda: tasto_alzato("d"), "d")

# creo la funzione del gioco
def gioco():
    if tasti["w"]:
        personaggio.setheading(90)
        personaggio.forward(5)
    elif tasti["s"]:
        personaggio.setheading(-90)
        personaggio.forward(5)
    elif tasti["a"]:
        personaggio.setheading(180)
        personaggio.forward(5)
    elif tasti["d"]:
        personaggio.setheading(0)
        personaggio.forward(5)

    # controllo la posizione della turtle e le impedisco 
    # di andare oltre i 300
    if personaggio.xcor() > 300:
        personaggio.setx(290)
    if personaggio.xcor() < -300:
        personaggio.setx(-290)
        
    if personaggio.ycor() > 300:
        personaggio.sety(290)
    if personaggio.ycor() < -300:
        personaggio.sety(-290)

    turtle.update()
    schermo.ontimer(gioco, 10)

gioco()

schermo.mainloop()