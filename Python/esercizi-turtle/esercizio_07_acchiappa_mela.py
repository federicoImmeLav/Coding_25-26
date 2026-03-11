import turtle
import random

# ╔══════════════════════════════════════════════════╗
# ║       ESERCIZIO 7 – Acchiappa la Mela! 🍎        ║
# ║              ⭐⭐⭐⭐ Livello: Alto                ║
# ╚══════════════════════════════════════════════════╝
#
# Un classico! Muovi il personaggio con le frecce
# e raccogli le mele prima che scadano.
#
# NOVITÀ: controllo da tastiera e ciclo di gioco
# ─────────────────────────────────────────────────
#   schermo.listen()
#       → attiva l'ascolto della tastiera
#
#   schermo.onkey(funzione, "Right")
#       → chiama funzione quando premi freccia destra
#       Tasti: "Right", "Left", "Up", "Down"
#              "space", "Return", "Escape"
#
#   schermo.ontimer(funzione, 100)
#       → chiama funzione dopo 100 millisecondi
#       Usato per creare il LOOP del gioco!
#
#   t.distance(altra_turtle)
#       → distanza tra due turtle objects
# ─────────────────────────────────────────────────
#
# STRUTTURA DEL GIOCO:
# ─────────────────────────────────────────────────
#   giocatore  → si muove con le frecce
#   mela       → appare in posizioni casuali
#   punteggio  → +1 ogni mela raccolta
#   vite       → -1 se la mela "scade" (cade fuori schermo)
# ─────────────────────────────────────────────────
#
# 📋 COSA FARE:
# ─────────────────────────────────────────────────
# TODO 1 → Completa muovi_su(), muovi_giu(),
#           muovi_sinistra(), muovi_destra():
#           usano t_giocatore.sety() e setx()
#           per muovere il giocatore di VELOCITA pixel.
#           Aggiungi anche il controllo dei bordi:
#           se x > 290: mettilo a -290 (esce a destra, rientra a sinistra)
#
# TODO 2 → Completa nuova_mela():
#           - posiziona t_mela in una posizione x casuale
#             in cima allo schermo (y = 220)
#           - cancella e ridisegna il simbolo "🍎"
#             con t_mela.write("🍎", ...)
#
# TODO 3 → Completa loop_gioco():
#           È il cuore del gioco! Viene chiamata ogni
#           TICK millisecondi. Deve:
#           a) far scendere la mela di VELOCITA_MELA pixel
#           b) controllare se il giocatore ha preso la mela
#              (distanza < 40) → punteggio +1, nuova mela
#           c) controllare se la mela è uscita in basso
#              (y < -230) → vite -1, nuova mela
#           d) se vite == 0: game over
#           e) aggiornare il testo in alto
#           f) richiamare se stessa: schermo.ontimer(loop_gioco, TICK)
#
# TODO 4 → SFIDA: fai accelerare la mela ogni 5 punti!
#           Usa una variabile globale VELOCITA_MELA
#           e aumentala di 0.5 ogni volta che:
#           punteggio % 5 == 0 and punteggio > 0
# ─────────────────────────────────────────────────

# --- SETUP ---
schermo = turtle.Screen()
schermo.title("Acchiappa la Mela! 🍎")
schermo.bgcolor("#1a1a2e")
schermo.setup(640, 500)
schermo.tracer(0)

VELOCITA = 20
VELOCITA_MELA = 3   # TODO 4: diventa globale e aumenta
TICK = 50           # ms tra ogni frame

punteggio = 0
vite = 3
gioco_attivo = True


# ── TURTLE: Giocatore ─────────────────────────────
t_giocatore = turtle.Turtle()
t_giocatore.hideturtle()
t_giocatore.penup()
t_giocatore.goto(0, -180)
t_giocatore.speed(0)


def disegna_giocatore():
    t_giocatore.clear()
    t_giocatore.write("🧑", align="center",
                      font=("Arial", 28, "normal"))


# ── TURTLE: Mela ──────────────────────────────────
t_mela = turtle.Turtle()
t_mela.hideturtle()
t_mela.penup()
t_mela.speed(0)


# ── TURTLE: HUD (punteggio e vite) ────────────────
t_hud = turtle.Turtle()
t_hud.hideturtle()
t_hud.penup()
t_hud.speed(0)


def aggiorna_hud():
    t_hud.clear()
    # Punteggio in alto a sinistra
    t_hud.goto(-300, 210)
    t_hud.pencolor("white")
    t_hud.write(f"Punti: {punteggio}",
                font=("Arial", 16, "bold"))
    # Vite in alto a destra
    t_hud.goto(180, 210)
    t_hud.write("❤️ " * vite,
                font=("Arial", 16, "normal"))


# ── MOVIMENTI ─────────────────────────────────────
def muovi_su():
    if not gioco_attivo: return
    y = t_giocatore.ycor()
    # TODO 1a → if y < 210: t_giocatore.sety(y + VELOCITA)
    disegna_giocatore()
    schermo.update()

def muovi_giu():
    if not gioco_attivo: return
    y = t_giocatore.ycor()
    # TODO 1b → if y > -210: t_giocatore.sety(y - VELOCITA)
    disegna_giocatore()
    schermo.update()

def muovi_destra():
    if not gioco_attivo: return
    x = t_giocatore.xcor()
    # TODO 1c → nuova_x = x + VELOCITA
    #           if nuova_x > 290: nuova_x = -290
    #           t_giocatore.setx(nuova_x)
    disegna_giocatore()
    schermo.update()

def muovi_sinistra():
    if not gioco_attivo: return
    x = t_giocatore.xcor()
    # TODO 1d → nuova_x = x - VELOCITA
    #           if nuova_x < -290: nuova_x = 290
    #           t_giocatore.setx(nuova_x)
    disegna_giocatore()
    schermo.update()


# ── NUOVA MELA ────────────────────────────────────
def nuova_mela():
    t_mela.clear()
    # TODO 2 → x = random.randint(-280, 280)
    #           t_mela.goto(x, 220)
    #           t_mela.write("🍎", align="center",
    #                        font=("Arial", 28, "normal"))
    pass


# ── LOOP DEL GIOCO ────────────────────────────────
def loop_gioco():
    global punteggio, vite, gioco_attivo, VELOCITA_MELA

    if not gioco_attivo:
        return

    # TODO 3a → fai scendere la mela
    # y_mela = t_mela.ycor()
    # t_mela.sety(y_mela - VELOCITA_MELA)
    # t_mela.clear()
    # t_mela.write("🍎", align="center", font=("Arial", 28, "normal"))

    # TODO 3b → controlla se il giocatore ha preso la mela
    # dist = t_giocatore.distance(t_mela)
    # if dist < 40:
    #     punteggio += 1
    #     nuova_mela()
    #     # TODO 4: aumenta VELOCITA_MELA ogni 5 punti

    # TODO 3c → controlla se la mela è uscita in basso
    # if t_mela.ycor() < -230:
    #     vite -= 1
    #     nuova_mela()

    # TODO 3d → game over
    # if vite <= 0:
    #     gioco_attivo = False
    #     game_over()
    #     return

    aggiorna_hud()
    schermo.update()

    # TODO 3f → riprogramma il loop
    # schermo.ontimer(loop_gioco, TICK)


# ── GAME OVER ─────────────────────────────────────
def game_over():
    t_hud.clear()
    t_hud.goto(0, 20)
    t_hud.pencolor("#ff6b6b")
    t_hud.write("GAME OVER", align="center",
                font=("Arial", 40, "bold"))
    t_hud.goto(0, -30)
    t_hud.pencolor("white")
    t_hud.write(f"Punteggio finale: {punteggio}",
                align="center", font=("Arial", 20, "normal"))
    schermo.update()


# ── AVVIO ─────────────────────────────────────────
schermo.listen()
schermo.onkey(muovi_su,       "Up")
schermo.onkey(muovi_giu,      "Down")
schermo.onkey(muovi_destra,   "Right")
schermo.onkey(muovi_sinistra, "Left")

disegna_giocatore()
nuova_mela()
aggiorna_hud()
loop_gioco()   # TODO 3f → decommentare schermo.ontimer per farlo girare!

schermo.mainloop()
