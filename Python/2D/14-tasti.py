# dizionari: creo una simulazione di stanza con le rispettive luci
# se True è accesa, se False è spenta
# luci = {
#     "camera": False,
#     "bagno": False,
#     "cinema": False,
#     "piscina": False,
#     "cucina": False
# }
# # per accendere una luce devo cambiare il valore di una stanza
# luci["cucina"] = True
# # posso però creare una funzione che a seconda della stanza
# # che indico, accende solo in quella
# def accendi(stanza):
#     luci[stanza] = True
# accendi("bagno")
##############################################################
# creo programma che si accorge quando tengo premuto un tasto
# fino a quando tengo premuto a, la turtle è rossa, quando
# la mollo torna nera

import turtle
# creo la schermata di gioco
s = turtle.Screen()
s.listen()

# creo la turtle
t = turtle.Turtle()
t.shape("turtle")

# creo il dizionario per i tasti
tasti = {
    "a": False,
    "Up": False,
    "Down": False,
    "Right": False,
    "Left": False
}

# devo creare le funzioni che fanno cambiare il valore
# del tasto da False a True e viceversa
def tasto_premuto(tasto):
    tasti[tasto] = True

def tasto_alzato(tasto):
    tasti[tasto] = False

# associare il tasto alla funzione che lo attiva
s.onkeypress(lambda: tasto_premuto("a"), "a")
s.onkeypress(lambda: tasto_premuto("Up"), "Up")

s.onkeyrelease(lambda: tasto_alzato("a"), "a")
s.onkeyrelease(lambda: tasto_alzato("Up"), "Up")

# ora devo far si che se il "a" è True la turtle 
# diventa rossa, altrimenti torna nera
def cambia_colore():
    if tasti["a"]:
        t.color("red")
    else:
        t.color("black")
    # chiamo la funzione ogni millisecodno che passa
    s.ontimer(cambia_colore,1)

# creo la funzione che fa funzionare i tasti per muoversi
# right (0), left (180), down (270)
def movimento():
    if tasti["Up"]:
        t.setheading(90) # punto verso l'alto
        t.forward(5)
    s.ontimer(movimento,1)

# faccio partire movimento
movimento()

# faccio partire cambia_colore
cambia_colore()
# comando per tenere la schermata aperta
s.mainloop()
