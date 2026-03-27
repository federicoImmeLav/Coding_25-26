# importare la libreria
import turtle

# creo la schermata di gioco
schermo = turtle.Screen()
# gioco che si aspetta che noi facciamo qualcosa
schermo.listen() 

# aggiungo una turtle
pg1 = turtle.Turtle()
# muovo il personaggio in avanti
pg1.forward(100)
# giro a destra di 90 gradi
pg1.right(90)
pg1.forward(100)
pg1.right(90)
pg1.forward(100)
pg1.right(90)
pg1.forward(100)

# faccio girare la turtle nella direzione che voglio io
pg1.setheading(135)
# stacco la turtle dallo schermo
pg1.penup()
pg1.forward(200)
# riabbasso la turtle sullo schermo
pg1.pendown()
pg1.setheading(0)

# cambio il colore
pg1.color("red")

for i in range(4):
    pg1.forward(100)
    pg1.right(90)

# comando che tiene aperta la schermata
schermo.mainloop()