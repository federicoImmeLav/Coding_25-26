# equazione della parabola y = a x *2 + b x + c
# a seconda dei numeri che ci sono in a b e c la parabola
import turtle

# python mi chiede i 3 parametri

a = int(input("Dimmi il valore di a: "))
b = int(input("Dimmi il valore di b: "))
c = int(input("Dimmi il valore di c: "))

schermo = turtle.Screen()
# personalizzo la dimensione della schermata
schermo.setup(width=500, height=700)
schermo.listen()

# a = (10,30)
# b = (50,30)

# turtle per assi cartesiani
assi = turtle.Turtle()
assi.teleport(0,-300)
assi.color("green")
assi.goto(0,300)
assi.teleport(-300,0)
assi.goto(300,0)
assi.hideturtle()

matita = turtle.Turtle()
matita.penup()
matita.shapesize(2)
matita.hideturtle()
# matita.goto(a)
# matita.pendown()
# matita.goto(b)

# equazione di una retta y = 3x + 1

x = -20
while x < 20:
    y = a * x **2 + b * x + c
    matita.goto(x, y / 10)
    matita.pendown()
    x += 2

schermo.mainloop()