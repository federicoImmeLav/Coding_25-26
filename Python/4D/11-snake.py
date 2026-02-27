import turtle
import random # libreria a caso

turtle.tracer(0)
# creo la testa dello snake
testa = turtle.Turtle()
testa.shape("square")
testa.color("green") # colore
testa.penup() # non fa disegnare

# creo la mela
mela = turtle.Turtle()
mela.shape("circle")
mela.color("red")
mela.penup()
mela.goto(0, 100)

# creo il corpo del serpente
corpo = []

# creo la schermata
s = turtle.Screen()
s.listen()

# dizionario dei tasti
tasti = {
    "w": False,
    "s": False,
    "a": False,
    "d": False
}

# funzione che accende il pulsante quando lo premo
def tasto_premuto(tasto):
    tasti[tasto] = True
# funzione che spenge il pulsante quando lo rilascio
def tasto_alzato(tasto):
    tasti[tasto] = False

s.onkeypress(lambda: tasto_premuto("w"), "w")
s.onkeypress(lambda: tasto_premuto("a"), "a")
s.onkeypress(lambda: tasto_premuto("s"), "s")
s.onkeypress(lambda: tasto_premuto("d"), "d")

s.onkeyrelease(lambda: tasto_alzato("w"), "w")
s.onkeyrelease(lambda: tasto_alzato("a"), "a")
s.onkeyrelease(lambda: tasto_alzato("s"), "s")
s.onkeyrelease(lambda: tasto_alzato("d"), "d")

# funzione del movimento
def movimento():
    if tasti["w"]:
        testa.setheading(90) # punta in alto
        testa.forward(20)
    elif tasti["s"]:
        testa.setheading(270) # punta in basso
        testa.forward(20)
    elif tasti["a"]:
        testa.setheading(180) # punta a sinistra
        testa.forward(20)
    elif tasti["d"]:
        testa.setheading(0)
        testa.forward(20)
    
    # se la testa è molto vicina alla mela la mela si sposta
    if testa.distance(mela) < 10:
        # sposto la mela di un numero casuale tra -280 e 280
        # su entrambe le coordinate
        mela.goto(random.randint(-280,280),random.randint(-280,280))
        # codice che crea turtle quadrate e le mette nel corpo
        pezzo = turtle.Turtle()
        pezzo.shape("square")
        pezzo.color("dark green")
        pezzo.penup()
        corpo.append(pezzo)

    for i in range(len(corpo)-1, 0, -1):
        corpo[i].goto(corpo[i-1].xcor(),corpo[i-1].ycor())
    
    if corpo:
        corpo[0].goto(testa.xcor(), testa.ycor())

    turtle.update()
    s.ontimer(movimento, 10)

# chiamare le funzione movimento
movimento()    

# schermata sempre aperta
s.mainloop()