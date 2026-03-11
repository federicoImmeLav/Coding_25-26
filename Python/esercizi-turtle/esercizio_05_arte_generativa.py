import turtle
import random

# ╔══════════════════════════════════════════════════╗
# ║       ESERCIZIO 5 – Arte generativa              ║
# ║              ⭐⭐⭐ Livello: Medio                 ║
# ╚══════════════════════════════════════════════════╝
#
# Usiamo cicli ANNIDATI (for dentro for) e random
# per creare pattern sempre diversi!
#
# NOVITÀ: random
# ─────────────────────────────────────────────────
#   import random
#
#   random.randint(1, 10)    → numero intero da 1 a 10
#   random.choice(lista)     → elemento casuale da lista
#   random.uniform(0.5, 2.0) → numero decimale casuale
#
# CICLI ANNIDATI:
# ─────────────────────────────────────────────────
#   for riga in range(5):          # 5 righe
#       for colonna in range(5):   # 5 colonne per riga
#           disegna_qualcosa()
#           t.forward(50)          # sposta a destra
#       vai_alla_prossima_riga()   # torna a sinistra, scendi
# ─────────────────────────────────────────────────
#
# 📋 COSA FARE:
# ─────────────────────────────────────────────────
# TODO 1 → Completa griglia_cerchi():
#           - ciclo esterno: 5 righe
#           - ciclo interno: 5 cerchi per riga
#           - ogni cerchio: raggio casuale tra 10 e 25
#           - ogni cerchio: colore casuale da COLORI
#           - dopo ogni cerchio: sposta di 80px a destra
#           - dopo ogni riga: torna a sinistra e scendi di 80px
#
# TODO 2 → Completa fiocco_neve(x, y, lunghezza):
#           Un ramo del fiocco = linea + due rami laterali.
#           Ripetilo 6 volte ruotando di 60°.
#           (Schema: forward, back, right, forward, back,
#            left, left, forward, back, right, home...)
#           Semplificazione: disegna 6 linee ruotando di 60°
#           da un punto centrale.
#
# TODO 3 → Completa campo_stelle():
#           - usa un ciclo for con range(30)
#           - per ogni stella: posizione casuale,
#             dimensione casuale tra 10 e 40
#             colore casuale
# ─────────────────────────────────────────────────
# 🎨 SFIDA EXTRA:
#    Modifica griglia_cerchi() per disegnare forme
#    diverse in base alla riga:
#    riga 0: cerchi  |  riga 1: quadrati  |  riga 2: triangoli...

# --- SETUP ---
schermo = turtle.Screen()
schermo.title("Esercizio 5 – Arte generativa")
schermo.bgcolor("#0d0d0d")
schermo.tracer(0)   # disattiva animazione per velocità

t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.speed(0)

COLORI = ["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff",
          "#ff922b", "#cc5de8", "#20c997", "#f06595"]


# ── FUNZIONE 1: Griglia di cerchi ─────────────────
def griglia_cerchi():
    RIGHE = 5
    COLONNE = 5
    PASSO = 80
    x_inizio = -200
    y_inizio = 160

    # TODO 1 → cicli annidati
    # for riga in range(RIGHE):
    #     for col in range(COLONNE):
    #         ...
    pass


# ── FUNZIONE 2: Fiocco di neve ────────────────────
def fiocco_neve(x, y, lunghezza):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("white")

    # Un fiocco = 6 raggi ruotati di 60°
    # TODO 2 → for i in range(6):
    #               t.forward(lunghezza)
    #               t.backward(lunghezza)
    #               t.right(60)
    for i in range(6):
        t.forward(lunghezza)
        t.backward(lunghezza)
        t.right(60)   # ← già fatto! Aggiungi il pencolor casuale sopra


# ── FUNZIONE 3: Campo di stelle ───────────────────
def stella_piccola(x, y, dim, colore):
    """Disegna una stellina a 5 punte."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(colore)
    t.fillcolor(colore)
    t.begin_fill()
    for _ in range(5):
        t.forward(dim)
        t.right(144)
    t.end_fill()


def campo_stelle():
    # TODO 3 → for i in range(30):
    #     x = random.randint(-280, 280)
    #     y = random.randint(-200, 200)
    #     dim = random.randint(10, 40)
    #     colore = random.choice(COLORI)
    #     stella_piccola(x, y, dim, colore)
    pass


# ── MAIN ──────────────────────────────────────────
def main():
    # Scegli quale funzione vuoi vedere!
    # Commentane alcune e lasciane una attiva.

    griglia_cerchi()

    # campo_stelle()

    # Fiocchi di neve (sfondo scuro consigliato)
    # for _ in range(10):
    #     fx = random.randint(-300, 300)
    #     fy = random.randint(-200, 200)
    #     fl = random.randint(20, 60)
    #     fiocco_neve(fx, fy, fl)

    schermo.update()   # aggiorna schermo (serve con tracer(0))


main()
schermo.mainloop()
