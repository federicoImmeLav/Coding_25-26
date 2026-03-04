import turtle

# creare una turtle
t = turtle.Turtle()
t.shape("turtle")

# creare la schermata
s = turtle.Screen()

# creo un quadrato (ripeto 4 volte la stessa azione)
def quadrato():
    for i in range(4):
        t.forward(100)
        t.right(90)

# scelgo colore del quadrato
t.fillcolor("green")
# per cambiare il colore del bordo
t.pencolor("red")
# per cambiare lo spessore del bordo
t.pensize(3)

# comando che dice dove si inizia a colorare
t.begin_fill()
# disegno quadrato
quadrato()
# comando che dice dove si smette di colorare
t.end_fill()

# tenere la schermata aperta
s.mainloop()

