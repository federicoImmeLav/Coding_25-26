import turtle
import time

schermo = turtle.Screen()

# creo il primo cerchio
t1 = turtle.Turtle()
t1.shape("circle") 
t1.shapesize(5)
t1.color("gray")
t1.teleport(0,150)

t2 = turtle.Turtle()
t2.shape("circle") 
t2.shapesize(5)
t2.color("gray")
t2.teleport(0,0)

t3 = turtle.Turtle()
t3.shape("circle") 
t3.shapesize(5)
t3.color("gray")
t3.teleport(0, -150)

stato = "spento"

# creo funz che accende il semaforo
def semaforo():
    global stato
    if stato == "spento":
        t1.color("red")
        t2.color("gray")
        stato = "rosso"

    elif stato == "rosso":
        t1.color("gray")
        t3.color("green")
        stato = "verde"

    elif stato == "verde":
        t3.color("gray")
        t2.color("orange")
        stato = "spento"

def lampeggio():
    global stato
    stato = "lamp"
    t1.color("gray")
    t3.color("gray")

    while stato == "lamp":
        t2.color("orange")
        time.sleep(0.4)
        t2.color("gray")
        time.sleep(0.4)

def reset():
    global stato
    stato = "spento"
    t1.color("gray")
    t2.color("gray")
    t3.color("gray")

# quando clicco sullo spazio accendo semaforo
schermo.listen()
schermo.onkey(semaforo,"space")
schermo.onkey(lampeggio, "a")
schermo.onkey(reset, "r")

schermo.mainloop()
