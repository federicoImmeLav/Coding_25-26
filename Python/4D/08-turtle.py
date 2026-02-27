# # importare la libreria
# import turtle
# # configuro il comando per funzionare
# t = turtle.Turtle()

# t.shape("turtle")
# # muovo la turtle avanti
# # t.forward(100)
# # # giro verso destra di 90 gradi
# # t.right(90)
# # t.forward(100)
# # t.right(90)

# # t.forward(100)
# # t.right(90)

# # t.forward(100)
# # t.right(90)

# # cambio il colore della turtle
# t.color("red")
# # al posto di scrivere 4 volte la stessa cosa, uso for
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# # per far vedere il disegno
# turtle.done()
#################################################################
# creo un programma che mi chiede quanto grande voglio
# il quadrato e dopo che ho risposto lo fa delle misure
# che dico io
# lato = int(input("Quanto misura il lato? "))

# # tutta la parte interattiva deve succedere prima di
# # importare la turtle
# import turtle
# t = turtle.Turtle()

# for i in range(4):
#     t.forward(lato)
#     t.right(90)


# turtle.done()

#########################################################
# import turtle
# t = turtle.Turtle()

# # creo la funzione generica che disegna i quadrati
# def quadrato(lato):
#     for i in range(4):
#         t.forward(lato)
#         t.right(90)

# t.shape("turtle")
# t.speed(0) # velocità della turtle
# t.color("purple")
# quadrato(200)

# # alzo la turtle così non disegna
# t.penup()

# # ruoto e sposto la turtle in un altro punto del disegno
# t.right(220)
# t.forward(200)

# # cambio colore alla turtle
# t.color("green")
# # rimetto la penna giu
# t.pendown()
# # raddrizzo la turtle
# t.right(140)
# # disegno quadrato grande 40
# quadrato(40)

# turtle.done()
#####################################################################
# import turtle
# t = turtle.Turtle()

# def triangolo(lato):
#     for i in range(3):
#         t.forward(lato)
#         t.right(120) # con 120 faccio un triangolo

# triangolo(100)

# turtle.done()


# x = 5

# def cambia():
#     global x
#     x = 10

# cambia()
# print(x)

import random

numeri = [1,5,3,8,9,2,7]

numero_a_caso = random.randint(1,100)
print(numero_a_caso)

# scelta = random.choice(numeri)

# print(scelta)