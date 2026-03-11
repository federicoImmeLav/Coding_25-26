import turtle
import random

# ╔══════════════════════════════════════════════════╗
# ║       ESERCIZIO 6 – Clicca il cerchio!           ║
# ║              ⭐⭐⭐ Livello: Medio                 ║
# ╚══════════════════════════════════════════════════╝
#
# Il primo vero giochino! 🎮
# Un cerchio colorato appare in una posizione casuale.
# Clicca su di esso prima che sparisca → +1 punto!
#
# NOVITÀ: eventi del mouse e scrittura testo
# ─────────────────────────────────────────────────
#   schermo.onclick(funzione)
#       → chiama "funzione(x, y)" quando clicchi
#
#   t.write("testo", font=("Arial", 20, "bold"))
#       → scrive testo nella posizione attuale
#
#   t.clear()
#       → cancella tutto ciò che ha disegnato questa turtle
#
#   t.distance(x, y)
#       → distanza tra la tartaruga e il punto (x,y)
#
# VARIABILI GLOBALI:
# ─────────────────────────────────────────────────
#   global punteggio
#   → dichiara che vuoi modificare una variabile
#     definita fuori dalla funzione
# ─────────────────────────────────────────────────
#
# 📋 COSA FARE:
# ─────────────────────────────────────────────────
# TODO 1 → Completa sposta_cerchio():
#           - genera x casuale tra -250 e 250
#           - genera y casuale tra -180 e 180
#           - usa t_cerchio.penup(), goto(x,y), pendown()
#           - disegna il cerchio pieno con begin_fill,
#             circle(RAGGIO), end_fill
#
# TODO 2 → Completa gestisci_click(x, y):
#           - calcola la distanza tra il click e il cerchio
#             con t_cerchio.distance(x, y)
#           - se la distanza è <= RAGGIO: è un HIT!
#             → incrementa punteggio di 1
#             → aggiorna la scritta del punteggio
#             → sposta il cerchio in una nuova posizione
#           - altrimenti: è un MISS (nessuna conseguenza,
#             o magari mostra un messaggio!)
#
# TODO 3 → Completa aggiorna_punteggio():
#           - cancella il testo precedente con t_testo.clear()
#           - posizionati in alto a sinistra (-280, 190)
#           - scrivi "Punti: " + str(punteggio) in bianco
#             font=("Arial", 18, "bold")
#
# TODO 4 → SFIDA: aggiungi un contatore di TENTATIVI
#           e mostra anche quante volte hai mancato.
#           Calcola e mostra la % di precisione!
# ─────────────────────────────────────────────────
# 💡 NOTA: usiamo DUE turtle separate:
#    t_cerchio → disegna il cerchio
#    t_testo   → scrive il punteggio
#    Così possiamo cancellare uno senza toccare l'altro!

# --- SETUP ---
schermo = turtle.Screen()
schermo.title("Clicca il cerchio! 🎯")
schermo.bgcolor("#1a1a2e")
schermo.setup(640, 480)

RAGGIO = 30
COLORI_CERCHIO = ["#ff6b6b", "#ffd93d", "#6bcb77",
                  "#4d96ff", "#cc5de8", "#ff922b"]

punteggio = 0
# TODO 4 → aggiungi: tentativi = 0

# Turtle per il cerchio
t_cerchio = turtle.Turtle()
t_cerchio.hideturtle()
t_cerchio.speed(0)
t_cerchio.pensize(2)

# Turtle per il testo del punteggio
t_testo = turtle.Turtle()
t_testo.hideturtle()
t_testo.penup()
t_testo.speed(0)


# ── FUNZIONE 1: Sposta e ridisegna il cerchio ─────
def sposta_cerchio():
    t_cerchio.clear()

    # TODO 1 → genera posizione casuale e disegna il cerchio
    colore = random.choice(COLORI_CERCHIO)
    t_cerchio.pencolor("white")
    t_cerchio.fillcolor(colore)

    # Esempio struttura:
    # x = random.randint(-250, 250)
    # y = random.randint(-180, 180)
    # t_cerchio.penup()
    # t_cerchio.goto(x, y)
    # t_cerchio.pendown()
    # t_cerchio.begin_fill()
    # t_cerchio.circle(RAGGIO)
    # t_cerchio.end_fill()
    pass


# ── FUNZIONE 2: Gestisci il click del mouse ───────
def gestisci_click(x, y):
    global punteggio
    # TODO 4 → global tentativi

    # TODO 2 → calcola distanza e controlla se è HIT
    # distanza = t_cerchio.distance(x, y)
    # if distanza <= RAGGIO:
    #     punteggio += 1
    #     aggiorna_punteggio()
    #     sposta_cerchio()
    pass


# ── FUNZIONE 3: Aggiorna testo punteggio ──────────
def aggiorna_punteggio():
    t_testo.clear()
    t_testo.penup()
    t_testo.goto(-280, 190)
    t_testo.pendown()
    # TODO 3 → scrivi il punteggio con t_testo.write(...)
    # t_testo.pencolor("white")
    # t_testo.write("Punti: " + str(punteggio),
    #               font=("Arial", 18, "bold"))
    pass


# ── AVVIO DEL GIOCO ───────────────────────────────
sposta_cerchio()
aggiorna_punteggio()

# Collega il click del mouse alla funzione
schermo.onclick(gestisci_click)

schermo.mainloop()
