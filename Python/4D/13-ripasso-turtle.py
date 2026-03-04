import turtle

# creo turtle
t = turtle.Turtle()
t.shape("turtle")

# creo la schermata
s = turtle.Screen()

# comando per cambiare la dimensione della turtle
# t.shapesize(3)

# funzione per disegnare un quadrato
def quadrato():
    for i in range(4):
        t.forward(100)
        t.right(90)

# decidere il colore con cui vogliamo colorare la figura
t.fillcolor("orange")
# comando per il colore del bordo/linea
t.pencolor("blue")
# comando per cambiare lo spessore del bordo
t.pensize(5)

# comando per iniziare a colorare
t.begin_fill()

quadrato()

# comando per smettere di colorare
t.end_fill()

# tengo la schemata aperta
s.mainloop()
