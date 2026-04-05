# importo tutti i comandi che servono
import turtle
import random
import time

# creo la schermata
schermo = turtle.Screen()
# per scegliere la grandezza della schermata
schermo.setup(width=700, height=700)
schermo.listen()

# inserisco turtle per la scritta di istruzioni
testo = turtle.Turtle()
testo.hideturtle()
testo.teleport(0,-300)
testo.write("Clicca sui bersagli nel minor tempo possibile", font=("Arial", 20), align="center")

# creo la turtle per il punteggio
punti = 15
resto = turtle.Turtle()
resto.hideturtle()
resto.teleport(-200,300)
resto.write(f"Bersagli rimanenti: {punti}", font=("Arial",20), align="center")

# creo turtle per il bersaglio
bers = turtle.Turtle()
# imposto bersaglio come tondo
bers.shape("circle")
bers.shapesize(2)
bers.color("red")

# creo la variabile del tempo
tempo_inizio = 0

# creo funzione che si accende quando clicco
def click(x,y):
    # dico alla funzione che sto usando punti
    global punti, tempo_inizio
    print(f"{x} e {y}")
    # se i punti sono 15 misuro il tempo
    if punti == 15:
        tempo_inizio = time.time()

    if bers.xcor() - 20 < x < bers.xcor() + 20 and bers.ycor() - 20 < y < bers.ycor() + 20:
        print("vicino")
        # punti a caso in cui mandare il cerchio
        x_bers = random.randint(-270,270)
        y_bers = random.randint(-270,270)
        # # sposto il cerchio nei posti casuali
        bers.teleport(x_bers, y_bers)
        punti -= 1 # diminuisco i bersagli
        resto.clear()
        resto.write(f"Bersagli rimanenti: {punti}", font=("Arial",20), align="center")

    if punti == 0:
        tempo_fine = time.time()
        tempo_totale = tempo_fine - tempo_inizio
        bers.hideturtle()
        resto.clear()
        testo.clear()
        resto.teleport(0,0)
        resto.write(f"Fine, ci hai messo {tempo_totale:.2f} secondi", font=("Arial", 20), align="center")   

# comando che si accorge che clicchiamo sullo schermo
schermo.onscreenclick(click)

# tenere gioco aperto
schermo.mainloop()