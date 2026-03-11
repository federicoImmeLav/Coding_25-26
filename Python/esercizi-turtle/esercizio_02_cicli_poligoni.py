import turtle

# ╔══════════════════════════════════════════════════╗
# ║       ESERCIZIO 2 – Cicli e poligoni             ║
# ║              ⭐⭐ Livello: Facile/Medio           ║
# ╚══════════════════════════════════════════════════╝
#
# Con un ciclo for possiamo disegnare poligoni
# in modo molto più elegante!
#
# IDEA CHIAVE:
# ─────────────────────────────────────────────────
#   Un poligono con N lati:
#   → ogni lato: t.forward(lunghezza)
#   → ogni angolo: t.right(360 / N)
#
#   Esempio – quadrato (N=4):
#   for i in range(4):
#       t.forward(100)
#       t.right(360 / 4)   # = 90°
#
#   Esempio – esagono (N=6):
#   for i in range(6):
#       t.forward(80)
#       t.right(360 / 6)   # = 60°
# ─────────────────────────────────────────────────
#
# 📋 COSA FARE:
# ─────────────────────────────────────────────────
# TODO 1 → Completa disegna_poligono(n_lati, lato):
#           usa un ciclo for con range(n_lati)
#           dentro: forward(lato) e right(360/n_lati)
#
# TODO 2 → Completa il ciclo nella funzione spirale():
#           ad ogni iterazione la lunghezza aumenta
#           di 5 pixel (lunghezza = lunghezza + 5)
#           e si gira sempre a destra di 89°
#
# TODO 3 → Nel main, chiama disegna_poligono per
#           disegnare: un triangolo (3), un quadrato (4),
#           un pentagono (5) e un esagono (6).
#           Usa goto() per spostarli in giro per lo schermo.
#
# TODO 4 → Aggiungi un ciclo for che cambia colore
#           a ogni lato del poligono usando la lista:
#           colori = ["red", "orange", "blue", "green",
#                     "purple", "pink", "cyan", "yellow"]
#           Suggerimento: t.pencolor(colori[i % len(colori)])
# ─────────────────────────────────────────────────

# --- SETUP ---
schermo = turtle.Screen()
schermo.title("Esercizio 2 – Cicli e poligoni")
schermo.bgcolor("#1a1a2e")

t = turtle.Turtle()
t.speed(10)
t.pensize(2)

colori = ["red", "orange", "blue", "green",
          "purple", "pink", "cyan", "yellow"]


# ── FUNZIONE 1: Disegna un poligono regolare ─────
def disegna_poligono(n_lati, lato):
    # TODO 1 → Scrivi il ciclo for qui
    # for i in range(???):
    #     ...
    pass   # ← cancella questo "pass" quando scrivi il codice


# ── FUNZIONE 2: Spirale quadrata ─────────────────
def spirale():
    t.penup()
    t.goto(100, 100)
    t.pendown()

    lunghezza = 5
    # TODO 2 → Completa il ciclo (100 iterazioni)
    for i in range(100):
        t.pencolor(colori[i % len(colori)])
        t.forward(lunghezza)
        t.right(89)
        # TODO 2 → aggiungi: lunghezza = lunghezza + 5


# ── MAIN ─────────────────────────────────────────
def main():
    # TODO 3 → Disegna qui almeno 3 poligoni diversi
    # Esempio:
    t.penup()
    t.goto(-200, 50)
    t.pendown()
    disegna_poligono(3, 80)   # triangolo

    # Aggiungi quadrato, pentagono, esagono...

    # Poi disegna la spirale:
    spirale()


main()
schermo.mainloop()
