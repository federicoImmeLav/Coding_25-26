import turtle

# ╔══════════════════════════════════════════════════╗
# ║       ESERCIZIO 3 – Fill e colori                ║
# ║              ⭐⭐ Livello: Facile/Medio           ║
# ╚══════════════════════════════════════════════════╝
#
# Finora abbiamo disegnato solo contorni.
# Ora impariamo a RIEMPIRE le forme di colore!
#
# COMANDI FILL:
# ─────────────────────────────────────────────────
#   t.fillcolor("yellow")   → imposta il colore di riempimento
#   t.begin_fill()          → inizia a registrare la forma
#   ... disegna la forma ...
#   t.end_fill()            → riempie la forma disegnata
#
#   SCHEMA SEMPRE UGUALE:
#   t.fillcolor("colore")
#   t.begin_fill()
#      ← qui disegni la forma ←
#   t.end_fill()
#
# COLORI UTILI:
#   "red", "blue", "green", "yellow", "orange",
#   "purple", "pink", "cyan", "white", "black",
#   "#ff6b35"  ← si possono usare anche i codici hex!
# ─────────────────────────────────────────────────
#
# 📋 COSA FARE:
# ─────────────────────────────────────────────────
# TODO 1 → Completa disegna_sole():
#           - Il cerchio centrale (t.circle(40)) deve
#             essere giallo pieno
#           - Aggiungi begin_fill() e end_fill()
#             attorno al disegno
#
# TODO 2 → Completa disegna_casa():
#           - Il rettangolo (corpo casa) deve essere
#             marrone: "#8B4513"
#           - Il tetto (triangolo) deve essere rosso
#           - Entrambe le parti devono avere il fill
#
# TODO 3 → Crea da zero la funzione disegna_albero()
#           Un albero semplice è:
#           - Un tronco: rettangolo marrone stretto
#           - Una chioma: triangolo verde (o cerchio)
#           Posizionalo a destra della casa con goto()
#
# TODO 4 → Crea disegna_nuvola() usando 3 cerchi
#           sovrapposti bianchi (o light blue).
#           Suggerimento: 3x t.circle(30) vicini!
# ─────────────────────────────────────────────────
# 💡 NOTA SUL CERCHIO:
#    t.circle(r) disegna un cerchio di raggio r.
#    La tartaruga parte dal BASSO del cerchio.
#    Posizionati con goto() dove vuoi il fondo del cerchio.

# --- SETUP ---
schermo = turtle.Screen()
schermo.title("Esercizio 3 – Fill e colori")
schermo.bgcolor("lightblue")

t = turtle.Turtle()
t.speed(8)
t.pensize(2)
t.hideturtle()   # nasconde la freccia durante il disegno


# ── FUNZIONE 1: Sole ──────────────────────────────
def disegna_sole():
    t.penup()
    t.goto(150, 120)
    t.pendown()

    t.pencolor("orange")
    # TODO 1 → aggiungi fillcolor, begin_fill, circle(40), end_fill
    t.circle(40)


# ── FUNZIONE 2: Casa ──────────────────────────────
def disegna_casa():
    # Corpo della casa (rettangolo 120x90)
    t.penup()
    t.goto(-60, -100)
    t.pendown()

    t.pencolor("#5a3010")
    # TODO 2a → fillcolor("#8B4513"), begin_fill
    for _ in range(2):
        t.forward(120)
        t.left(90)
        t.forward(90)
        t.left(90)
    # TODO 2a → end_fill

    # Tetto (triangolo sopra la casa)
    t.penup()
    t.goto(-60, -10)        # angolo sinistro della base del tetto
    t.pendown()
    t.setheading(0)         # punta a destra

    t.pencolor("darkred")
    # TODO 2b → fillcolor("red"), begin_fill
    t.forward(120)          # base del tetto
    t.left(120)
    t.forward(120)
    t.left(120)
    t.forward(120)
    # TODO 2b → end_fill


# ── FUNZIONE 3: Albero ────────────────────────────
def disegna_albero():
    # TODO 3 → Crea questa funzione da zero!
    # Tronco: rettangolo stretto (es. 20x60) marrone
    # Chioma: triangolo verde o cerchio verde sopra
    pass


# ── FUNZIONE 4: Nuvola ────────────────────────────
def disegna_nuvola():
    # TODO 4 → 3 cerchi bianchi sovrapposti
    # Suggerimento:
    # t.penup(); t.goto(-180, 130); t.pendown()
    # 3 volte: fillcolor("white"), begin_fill,
    #          circle(30), end_fill, penup, forward(25), pendown
    pass


# ── MAIN ──────────────────────────────────────────
def main():
    disegna_sole()
    disegna_casa()
    disegna_albero()
    disegna_nuvola()

    # Disegna il prato (rettangolo verde in fondo)
    t.penup()
    t.goto(-300, -100)
    t.pendown()
    t.pencolor("#2d5a1b")
    t.fillcolor("#3a7d22")
    t.begin_fill()
    for _ in range(2):
        t.forward(600)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()


main()
schermo.mainloop()
