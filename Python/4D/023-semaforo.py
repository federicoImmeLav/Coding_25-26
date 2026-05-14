import turtle
import time

s = turtle.Screen()

# creo i tre cerchi del samaforo
t1 = turtle.Turtle()
t1.shape("circle")
t1.shapesize(5)
t1.color("gray")
t1.teleport(0, 150)

t2 = turtle.Turtle()
t2.shape("circle")
t2.shapesize(5)
t2.color("gray")
t2.teleport(0, 0)

t3 = turtle.Turtle()
t3.shape("circle")
t3.shapesize(5)
t3.color("gray")
t3.teleport(0, -150)

# quando inizia il semaforo è spento
stato = "spento"

# creo la funzione che accende il semaforo
def semaforo():
    global stato
    if stato == "spento":
        t1.color("red")
        t2.color("gray")
        stato = "rosso"

    elif stato == "rosso":
        t3.color("green")
        t1.color("gray")
        stato = "verde"

    elif stato == "verde":
        t2.color("orange")
        t3.color("gray")
        stato = "spento"

def tilt():
    global stato
    stato = "tilt"
    t1.color("gray")
    t3.color("gray")
    while stato == "tilt":
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

s.listen()
s.onkey(semaforo, "space")
s.onkey(tilt, "t")
s.onkey(reset, "r")
s.mainloop()