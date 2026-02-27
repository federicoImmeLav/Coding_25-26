# dizionari, contenitore che ha diverse informazioni al
# suo interno
# studente = {
#     "nome": "Manuel",
#     "età": 18,
#     "promosso": True,
# }
# # stampo un valore del dizionario
# print(studente["nome"])
# print(studente["promosso"])

# # posso anche cambiare un valore del dizionario
# studente["nome"] = "Alessio"
# studente["promosso"] = False

# print(studente["nome"])
# print(studente["promosso"])
##########################################################
# luci in casa, True accese, False spente
# luci = {
#     "camera" : False,
#     "salotto" : False,
#     "cucina" : False,
#     "piscina" : False,
#     "sauna" : False,
#     "campo_tennis" : False
# }

# print(luci)
# # per accendere le luci devo cambiare il valore da False a True
# luci["cucina"] = True # accendo la luce in cucina

# # creare la funzione che accende le luci
# def accendi(stanza):
#     luci[stanza] = True

# accendi("sauna")
##############################################################
# faccio un programma che fa cambiare il colore della turtle
# finchè tengo premuto un pulsante, quando lo mollo il colore
# ricambia
import turtle

s = turtle.Screen() # aprire la schermata bianca
s.listen() # il programma aspetta che io faccia qualunque cosa

# creo la turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

# creo il dizionario per i tasti
#  False il tasto non è schiacciato, True sarà premuto
tasti = {
    "a" : False,
    "s" : False,
    "Up": False,
    "Down": False,
    "Right": False,
    "Left":False
}

# creo la funzione che mi cambia il tasto da False a True
def tasto_schiacciato(tasto):
    tasti[tasto] = True

def tasto_alzato(tasto):
    tasti[tasto] = False

# collegare i tasti alle funzioni, cioè devo mettere il comando
# per cui quando clicco il tasto, parte la funzione, e
# quando mollo il tasto parte l'altra funzione
s.onkeypress(lambda: tasto_schiacciato("a"), "a")
s.onkeypress(lambda: tasto_schiacciato("s"), "s")
s.onkeypress(lambda: tasto_schiacciato("Up"), "Up")
s.onkeypress(lambda: tasto_schiacciato("Down"), "Down")
s.onkeypress(lambda: tasto_schiacciato("Left"), "Left")
s.onkeypress(lambda: tasto_schiacciato("Right"), "Right")

s.onkeyrelease(lambda: tasto_alzato("a"), "a")
s.onkeyrelease(lambda: tasto_alzato("s"), "s")
s.onkeyrelease(lambda: tasto_alzato("Up"), "Up")
s.onkeyrelease(lambda: tasto_alzato("Down"), "Down")
s.onkeyrelease(lambda: tasto_alzato("Left"), "Left")
s.onkeyrelease(lambda: tasto_alzato("Right"), "Right")

# ora devo creare la funzione che cambia colore 
# finchè tengo premuto il tasto
# se il tasto è True, diventa verde, se il tasto è False, torna nera
def cambia_colore():
    if tasti["a"]:
        t.color("green")
    elif tasti["s"]:
        t.color("red")
    else:
        t.color("black")
    # comando che ripete questa funzione in loop
    s.ontimer(cambia_colore,1)

def movimento():
    if tasti["Up"]:
        t.setheading(90) # punto verso l'alto
        t.forward(5)
    elif tasti["Down"]:
        t.setheading(270)
        t.forward(5)
    elif tasti["Left"]:
        t.setheading(180)
        t.forward(5)
    elif tasti["Right"]:
        t.setheading(0)
        t.forward(5)

    s.ontimer(movimento,1)

movimento()
cambia_colore() # faccio partire la funzione

# rimanga la schermata aperta sempre
turtle.mainloop()