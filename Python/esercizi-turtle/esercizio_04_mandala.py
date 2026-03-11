import turtle

# ╔══════════════════════════════════════════════════╗
# ║       ESERCIZIO 4 – Mandala colorato             ║
# ║              ⭐⭐⭐ Livello: Medio                 ║
# ╚══════════════════════════════════════════════════╝
#
# Un mandala si crea ripetendo una forma tante volte
# ruotando di un angolo fisso ogni volta.
#
# IDEA CHIAVE:
# ─────────────────────────────────────────────────
#   Se voglio 12 petali attorno al centro:
#   → angolo di rotazione = 360 / 12 = 30°
#
#   for i in range(12):
#       disegna_petalo()
#       t.right(30)        # ruota per il prossimo
#
#   t.home() riporta la tartaruga al centro (0,0)
#   t.setheading(0) punta la tartaruga a destra (est)
# ─────────────────────────────────────────────────
#
# 📋 COSA FARE:
# ─────────────────────────────────────────────────
# TODO 1 → Completa petalo():
#           Un "petalo" è un cerchio piccolo (radius=50).
#           Dopo averlo disegnato, torna al centro:
#           t.penup(), t.home(), t.pendown()
#
# TODO 2 → Completa il ciclo in disegna_mandala():
#           - Quante ripetizioni? Usa la variabile N_PETALI
#           - Dopo ogni petalo ruota di 360/N_PETALI gradi
#           - Cambia il colore ad ogni iterazione con:
#             t.fillcolor(colori[i % len(colori)])
#
# TODO 3 → Completa stella():
#           Una stella si disegna avanzando e girando
#           di 144° per 5 volte (o 72° per 10 volte).
#           Aggiungi il fill con un colore a scelta.
#
# TODO 4 → Aggiungi un secondo anello di petali
#           PIÙ GRANDI (radius=90) sopra al primo,
#           con un numero diverso (es. N_PETALI2 = 8)
#           e colori diversi.
# ─────────────────────────────────────────────────
# 🎨 SFIDA EXTRA:
#    Prova a far variare il raggio del cerchio
#    ad ogni iterazione per creare un effetto
#    spirale nel mandala!

# --- SETUP ---
schermo = turtle.Screen()
schermo.title("Esercizio 4 – Mandala colorato")
schermo.bgcolor("black")

t = turtle.Turtle()
t.speed(0)       # 0 = velocità massima
t.pensize(1)
t.hideturtle()

N_PETALI = 12
colori = ["red", "orange", "yellow", "lime",
          "cyan", "blue", "purple", "pink",
          "magenta", "gold", "white", "lightblue"]


# ── FUNZIONE 1: Singolo petalo ────────────────────
def petalo(radius):
    t.pencolor("white")
    # TODO 1 → begin_fill, circle(radius), end_fill
    #           poi: penup, home, pendown
    t.circle(radius)     # ← già scritto, aggiungi fill attorno!


# ── FUNZIONE 2: Mandala ──────────────────────────
def disegna_mandala():
    t.penup()
    t.home()
    t.pendown()

    # TODO 2 → ciclo for con range(N_PETALI)
    #           dentro: fillcolor, petalo(50), right(360/N_PETALI)
    for i in range(N_PETALI):
        t.fillcolor(colori[i % len(colori)])
        petalo(50)
        t.right(360 / N_PETALI)
        # ↑ questo è già fatto! Aggiungi solo il fillcolor sopra


# ── FUNZIONE 3: Stella ───────────────────────────
def stella(dimensione):
    t.penup()
    t.home()
    t.pendown()

    t.pencolor("yellow")
    t.fillcolor("gold")
    t.begin_fill()
    # TODO 3 → for i in range(5):
    #               t.forward(dimensione)
    #               t.right(144)
    t.end_fill()


# ── FUNZIONE 4: Secondo anello (facoltativo) ─────
def secondo_anello():
    # TODO 4 → Copia la logica di disegna_mandala
    #           ma con radius=90 e N_PETALI2=8
    pass


# ── MAIN ──────────────────────────────────────────
def main():
    disegna_mandala()
    secondo_anello()    # TODO 4 (facoltativo)
    stella(60)          # La stella va sopra al mandala


main()
schermo.mainloop()
