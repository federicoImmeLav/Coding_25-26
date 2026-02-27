# importare la libreria
import turtle

# creo la tartaruga che disegna
t = turtle.Turtle()
t.shape("turtle") # forma della tartaruga

# ripetere 4 volte gli stessi comandi con for 
for i in range(4):
    t.forward(100) # vai avanti di 100
    t.right(90) # giro a destra di 90 gradi

# sposto indietro la turtle di 300 per disegnare altro
# alzo la turtle per non disegnare
t.penup()
t.backward(300)
t.pendown()

# disegno triangolo
for i in range(3):
    t.forward(100)
    t.right(120)

turtle.done()
############################################################
# creo la funzione per il quadrato
# def quadrato(lato):
#     t.pendown()
#     for i in range(4):
#         t.forward(lato)
#         t.right(90)
#     t.penup()

# # creo la funzione per il triangolo
# def triangolo(lato):
#     t.pendown()
#     for i in range(3):
#         t.forward(lato)
#         t.right(120)
#     t.penup()

# quadrato(200)

# t.backward(150)
# t.color("blue")

# triangolo(50)

# t.right(270)
# t.forward(200)
# t.color("red")

# quadrato(50)

######################################################################################
# regola geometrica per cui sapendo i lati di un poligono, possiamo sapere
# quanti devono valere gli angoli 
# la regola è che l'angolo vale 360 / n lati

# lato = int(input("Quanto deve valere il lato del poligono? "))
# n_lati = int(input("Quanti lati ha il poligono? "))

# angolo = 360 / n_lati

# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# def poligono(n_lati, lato, angolo):
#     for i in range(n_lati):
#         t.forward(lato)
#         t.right(angolo)

# # chiamo la funzione per disegnare
# poligono(n_lati, lato, angolo)

# # crea la schermata
# turtle.done()

