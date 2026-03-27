import turtle
import random

# creo la schermata
s = turtle.Screen()
s.listen()

# creo i cerchi che si illumineranno (7)
c1 = turtle.Turtle()
c1.penup()
c1.shape("circle")
c1.color("gray")
c1.shapesize(3)

c2 = turtle.Turtle()
c2.penup()
c2.shape("circle")
c2.color("gray")
c2.shapesize(3)
c2.goto(100, 0)

c3 = turtle.Turtle()
c3.penup()
c3.shape("circle")
c3.color("gray")
c3.shapesize(3)
c3.goto(100, 100)

c4 = turtle.Turtle()
c4.penup()
c4.shape("circle")
c4.color("gray")
c4.shapesize(3)
c4.goto(100, -100)

c5 = turtle.Turtle()
c5.penup()
c5.shape("circle")
c5.color("gray")
c5.shapesize(3)
c5.goto(-100, -100)

c6 = turtle.Turtle()
c6.penup()
c6.shape("circle")
c6.color("gray")
c6.shapesize(3)
c6.goto(-100, 100)

c7 = turtle.Turtle()
c7.penup()
c7.shape("circle")
c7.color("gray")
c7.shapesize(3)
c7.goto(-100, 0)

c8 = turtle.Turtle()
c8.penup()
c8.shape("circle")
c8.color("gray")
c8.shapesize(3)
c8.goto(0, 100)

c9 = turtle.Turtle()
c9.penup()
c9.shape("circle")
c9.color("gray")
c9.shapesize(3)
c9.goto(0, -100)

# testo di indicazioni
testo = turtle.Turtle()
testo.hideturtle()
testo.penup()
testo.goto(0,200)
testo.write("Premi SPAZIO per tirare il dado", font=("Arial", 20), align="center")

bordo = turtle.Turtle()
bordo.hideturtle()
bordo.penup()
bordo.goto(150, 150)
bordo.pendown()
for i in range(4):
    bordo.right(90)
    bordo.forward(300)

# creo la funzione che spegne tutte le turtle
def spegni():
    c1.color("white")
    c2.color("white")
    c3.color("white")
    c4.color("white")
    c5.color("white")
    c6.color("white")
    c7.color("white")
    c8.color("white")
    c9.color("white")

# creo funzioni che accendono i pallini corrispondenti ai numeri
def acc1():
    c1.color("red")

def acc2():
    c4.color("red")
    c6.color("red")

def acc3():
    acc2()
    c1.color("red")

def acc4():
    acc2()
    c3.color("red")
    c5.color("red")

def acc5():
    acc4()
    c1.color("red")

def acc6():
    acc4()
    c2.color("red")
    c7.color("red")

# funzione che quando premo spazio spegne tutte, sceglie una
# funz a caso e accende i pallini corrispondenti
# creo lista di 6 funzioni
funzioni = [acc1, acc2, acc3, acc4, acc5, acc6]
# creo funzione che lancia il dado
def dado():
    spegni()
    random.choice(funzioni)()

s.onkey(dado, "space")

s.mainloop()

