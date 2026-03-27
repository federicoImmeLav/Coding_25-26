import random
import turtle

s = turtle.Screen()
s.listen()

# lista di posizioni di tutti i cerchi
posizioni = [
    (0,0),
    (100,0),
    (-100,0),
    (100,100),
    (100,-100),
    (-100,-100),
    (-100,100),
    (0,100),
    (0,-100),
]
# per ogni coppia di coordinate creo un cerchio
# lista dei cerchi
cerchi = []
colore = "lightgray"

for x,y in posizioni:
    c = turtle.Turtle()
    c.shape("circle")
    c.color(colore)
    c.shapesize(3)
    c.penup()
    c.goto(x,y)
    cerchi.append(c)

# turtle che disegna il bordo
bordo = turtle.Turtle()
bordo.hideturtle()
bordo.teleport(150,150)
# disegno quadrato intorno
for i in range(4):
    bordo.right(90)
    bordo.forward(300)

# turtle che fa la scritta
testo = turtle.Turtle()
testo.hideturtle()
testo.teleport(0,200)
testo.write("Premi SPAZIO per tirare il dado", font=("Arial", 20), align="center")

# creo la funz che cambia il colore
def spegni():
    for c in cerchi:
        c.color("white")
    
# funzione che si accende quando premo spazio
def lancio():
    spegni()
    # creo un numero casuale da 1 a 6
    n = random.randint(1,6)
    for i in dado[n]:
        cerchi[i].color("red")

# creo associazione tra pallini e numeri
dado = {
    1: [0],
    2: [4,6],
    3: [0,4,6],
    4: [3,4,5,6],
    5: [0,3,4,5,6],
    6: [1,2,3,4,5,6],
}

s.onkey(lancio, "space")

s.mainloop()