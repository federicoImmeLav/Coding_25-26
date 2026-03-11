import turtle

# ╔══════════════════════════════════════════════════╗
# ║       ESERCIZIO 1 – Le prime forme               ║
# ║              ⭐ Livello: Facile                   ║
# ╚══════════════════════════════════════════════════╝
#
# Benvenuto nella Turtle! 🐢
# La tartaruga si muove sul foglio e disegna linee.
#
# COMANDI BASE da sapere:
# ─────────────────────────────────────────────────
#   t.forward(100)    → avanza di 100 pixel
#   t.backward(50)    → torna indietro di 50 pixel
#   t.right(90)       → gira a destra di 90 gradi
#   t.left(45)        → gira a sinistra di 45 gradi
#   t.penup()         → alza la penna (non disegna)
#   t.pendown()       → abbassa la penna (disegna)
#   t.goto(x, y)      → vai alle coordinate x, y
#   t.pencolor("red") → cambia colore del tratto
#   t.pensize(3)      → spessore della linea
#   t.speed(5)        → velocità (1=lento, 10=veloce)
# ─────────────────────────────────────────────────
#
# 📋 COSA FARE:
# ─────────────────────────────────────────────────
# TODO 1 → Completa la funzione disegna_quadrato()
#           aggiungendo i 3 lati mancanti
#           (il primo lato è già fatto come esempio)
#
# TODO 2 → Completa disegna_triangolo()
#           Un triangolo equilatero ha angoli di 120°
#           e 3 lati uguali. Il primo lato è già fatto.
#
# TODO 3 → Nella funzione disegna_tutto(), chiama
#           le due funzioni nell'ordine giusto.
#           Usa t.penup() e t.goto() per spostarti
#           tra una forma e l'altra senza lasciare traccia.
#
# TODO 4 → Cambia i colori: il quadrato in "blue"
#           e il triangolo in "green"
# ─────────────────────────────────────────────────
# 💡 SUGGERIMENTO:
#    Per un quadrato servono 4 lati con angolo 90°.
#    Per un triangolo servono 3 lati con angolo 120°.
#    Pensa: forward → right → forward → right → ...

# --- SETUP ---
schermo = turtle.Screen()
schermo.title("Esercizio 1 – Le prime forme")
schermo.bgcolor("white")

t = turtle.Turtle()
t.speed(5)
t.pensize(3)


# ── FUNZIONE 1: Disegna un quadrato ──────────────
def disegna_quadrato(lato):
    t.pencolor("red")       # TODO 4: cambia in "blue"
    t.forward(lato)         # Lato 1 ← già fatto!
    t.right(90)

    # TODO 1 → Aggiungi qui i lati 2, 3 e 4
    # (copia le due righe qua sopra altre 3 volte)


# ── FUNZIONE 2: Disegna un triangolo ─────────────
def disegna_triangolo(lato):
    t.pencolor("red")       # TODO 4: cambia in "green"
    t.forward(lato)         # Lato 1 ← già fatto!
    t.right(120)

    # TODO 2 → Aggiungi qui i lati 2 e 3


# ── FUNZIONE 3: Disegna tutto ────────────────────
def disegna_tutto():
    # Posizionati per il quadrato
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    disegna_quadrato(100)

    # TODO 3 → Spostati a destra (es. goto(50, 0))
    #           e chiama disegna_triangolo(100)


# ── AVVIA ────────────────────────────────────────
disegna_tutto()

schermo.mainloop()
