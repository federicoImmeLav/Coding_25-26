import turtle
import random

# ╔══════════════════════════════════════════════════╗
# ║       ESERCIZIO 8 – Evita le Bombe! 💣           ║
# ║              ⭐⭐⭐⭐ Livello: Alto                ║
# ╚══════════════════════════════════════════════════╝
#
# Il gioco più completo! Hai un razzo 🚀 che si
# muove su e giù (solo). Le bombe 💣 arrivano
# da destra verso sinistra. Evitale il più a lungo!
# Raccogliendo le stelle ⭐ guadagni punti.
#
# STRUTTURA (tutto già impostato, tu completi):
# ─────────────────────────────────────────────────
#   t_razzo    → il giocatore, si muove su/giù
#   bombe[]    → lista di turtle, arrivano da destra
#   t_stella   → una stella bonus che appare ogni tanto
#   t_hud      → punteggio e vite
# ─────────────────────────────────────────────────
#
# 📋 COSA FARE:
# ─────────────────────────────────────────────────
# TODO 1 → Completa muovi_razzo_su() e muovi_razzo_giu():
#           - limita il movimento tra y = -200 e y = 200
#           - ridisegna il razzo dopo ogni movimento
#
# TODO 2 → Completa aggiungi_bomba():
#           - crea una nuova Turtle
#           - posizionala a x=320, y casuale tra -180 e 180
#           - aggiungila alla lista BOMBE
#           - disegnala con il simbolo "💣"
#
# TODO 3 → Completa muovi_bombe():
#           - fai scorrere ogni bomba a sinistra di VEL_BOMBA
#           - ridisegna il simbolo "💣" dopo ogni spostamento
#           - se una bomba esce a sinistra (x < -320):
#             rimuovila dalla lista e distruggila
#
# TODO 4 → Completa controlla_collisioni():
#           - per ogni bomba: se distance(razzo) < 35 →
#             vite -= 1, rimuovi la bomba, se vite==0: game_over()
#           - per la stella: se distance(razzo) < 35 →
#             punteggio += 5, sposta la stella altrove
#
# TODO 5 → Completa loop_gioco():
#           a) muovi_bombe()
#           b) muovi_stella()
#           c) controlla_collisioni()
#           d) ogni SPAWN_OGNI frames, aggiungi_bomba()
#           e) incrementa punteggio di 1 ogni frame
#           f) aggiorna_hud()
#           g) schermo.update()
#           h) riprogramma con ontimer
#
# TODO 6 → SFIDA: aggiungi un secondo tipo di oggetto
#           "💊" che resetta le vite a 3 se raccolto!
# ─────────────────────────────────────────────────

# --- SETUP ---
schermo = turtle.Screen()
schermo.title("Evita le Bombe! 💣")
schermo.bgcolor("#0d0d1a")
schermo.setup(700, 520)
schermo.tracer(0)

# Costanti
VELOCITA_RAZZO = 25
VEL_BOMBA      = 5
TICK           = 40      # ms per frame (~25 FPS)
SPAWN_OGNI     = 30      # ogni quanti frame appare una bomba

# Variabili di stato
punteggio  = 0
vite       = 3
frame      = 0
gioco_attivo = True
BOMBE      = []          # lista di turtle-bombe


# ══════════════════════════════════════
#  TURTLE: RAZZO (giocatore)
# ══════════════════════════════════════
t_razzo = turtle.Turtle()
t_razzo.hideturtle()
t_razzo.penup()
t_razzo.goto(-280, 0)
t_razzo.speed(0)

def disegna_razzo():
    t_razzo.clear()
    t_razzo.write("🚀", align="center",
                  font=("Arial", 30, "normal"))

def muovi_razzo_su():
    if not gioco_attivo: return
    y = t_razzo.ycor()
    # TODO 1a → if y < 200: t_razzo.sety(y + VELOCITA_RAZZO)
    disegna_razzo()
    schermo.update()

def muovi_razzo_giu():
    if not gioco_attivo: return
    y = t_razzo.ycor()
    # TODO 1b → if y > -200: t_razzo.sety(y - VELOCITA_RAZZO)
    disegna_razzo()
    schermo.update()


# ══════════════════════════════════════
#  TURTLE: BOMBE
# ══════════════════════════════════════
def aggiungi_bomba():
    # TODO 2 → crea una nuova Turtle, posizionala,
    #           disegnala con "💣", aggiungila a BOMBE
    b = turtle.Turtle()
    b.hideturtle()
    b.penup()
    b.speed(0)
    # x = 320
    # y = random.randint(-180, 180)
    # b.goto(x, y)
    # b.write("💣", align="center", font=("Arial", 28, "normal"))
    # BOMBE.append(b)
    pass

def muovi_bombe():
    # TODO 3 → scorri ogni bomba a sinistra
    # for b in BOMBE[:]:   ← copia la lista per poterla modificare
    #     b.clear()
    #     b.setx(b.xcor() - VEL_BOMBA)
    #     b.write("💣", align="center", font=("Arial", 28, "normal"))
    #     if b.xcor() < -320:
    #         b.clear()
    #         b.hideturtle()
    #         BOMBE.remove(b)
    pass


# ══════════════════════════════════════
#  TURTLE: STELLA BONUS
# ══════════════════════════════════════
t_stella = turtle.Turtle()
t_stella.hideturtle()
t_stella.penup()
t_stella.speed(0)

def sposta_stella():
    t_stella.clear()
    x = random.randint(-200, 280)
    y = random.randint(-200, 200)
    t_stella.goto(x, y)
    t_stella.write("⭐", align="center",
                   font=("Arial", 26, "normal"))

def muovi_stella():
    # La stella scivola lentamente verso sinistra
    t_stella.clear()
    t_stella.setx(t_stella.xcor() - 1.5)
    t_stella.write("⭐", align="center",
                   font=("Arial", 26, "normal"))
    if t_stella.xcor() < -320:
        sposta_stella()


# ══════════════════════════════════════
#  HUD
# ══════════════════════════════════════
t_hud = turtle.Turtle()
t_hud.hideturtle()
t_hud.penup()
t_hud.speed(0)

def aggiorna_hud():
    t_hud.clear()
    t_hud.goto(-320, 225)
    t_hud.pencolor("white")
    t_hud.write(f"Punti: {punteggio}",
                font=("Arial", 15, "bold"))
    t_hud.goto(180, 225)
    cuori = "❤️ " * vite + "🖤 " * (3 - vite)
    t_hud.write(cuori, font=("Arial", 15, "normal"))


# ══════════════════════════════════════
#  COLLISIONI
# ══════════════════════════════════════
def controlla_collisioni():
    global punteggio, vite

    # TODO 4a → controlla bombe
    # for b in BOMBE[:]:
    #     if t_razzo.distance(b) < 35:
    #         vite -= 1
    #         b.clear()
    #         BOMBE.remove(b)
    #         aggiorna_hud()
    #         schermo.update()
    #         if vite <= 0:
    #             game_over()
    #             return

    # TODO 4b → controlla stella bonus
    # if t_razzo.distance(t_stella) < 35:
    #     punteggio += 5
    #     sposta_stella()
    pass


# ══════════════════════════════════════
#  LOOP DI GIOCO
# ══════════════════════════════════════
def loop_gioco():
    global punteggio, frame

    if not gioco_attivo:
        return

    frame += 1

    # TODO 5 → in ordine:
    # a) muovi_bombe()
    # b) muovi_stella()
    # c) controlla_collisioni()
    # d) if frame % SPAWN_OGNI == 0: aggiungi_bomba()
    # e) punteggio += 1
    # f) aggiorna_hud()
    # g) schermo.update()
    # h) schermo.ontimer(loop_gioco, TICK)

    # Per ora giriamo solo una volta, senza ontimer:
    aggiorna_hud()
    schermo.update()
    # ↑ Quando hai completato i TODO, decommentare l'ontimer!


# ══════════════════════════════════════
#  GAME OVER
# ══════════════════════════════════════
def game_over():
    global gioco_attivo
    gioco_attivo = False

    # Schermo rosso lampeggiante (simulato con sfondo)
    schermo.bgcolor("#3d0000")

    t_hud.clear()

    # Testo "GAME OVER"
    t_hud.goto(0, 60)
    t_hud.pencolor("#ff6b6b")
    t_hud.write("💥 GAME OVER 💥", align="center",
                font=("Arial", 36, "bold"))

    t_hud.goto(0, 0)
    t_hud.pencolor("white")
    t_hud.write(f"Punteggio: {punteggio}",
                align="center", font=("Arial", 22, "normal"))

    t_hud.goto(0, -50)
    t_hud.pencolor("#aaa")
    t_hud.write("Premi R per ricominciare",
                align="center", font=("Arial", 14, "normal"))

    schermo.update()


# ══════════════════════════════════════
#  RESTART
# ══════════════════════════════════════
def restart():
    global punteggio, vite, frame, gioco_attivo, BOMBE
    if gioco_attivo:
        return
    # Pulisci le bombe
    for b in BOMBE:
        b.clear()
    BOMBE = []
    # Reset stato
    punteggio = 0
    vite = 3
    frame = 0
    gioco_attivo = True
    schermo.bgcolor("#0d0d1a")
    t_razzo.goto(-280, 0)
    disegna_razzo()
    sposta_stella()
    aggiorna_hud()
    loop_gioco()


# ══════════════════════════════════════
#  AVVIO
# ══════════════════════════════════════
schermo.listen()
schermo.onkey(muovi_razzo_su,  "Up")
schermo.onkey(muovi_razzo_giu, "Down")
schermo.onkey(restart,         "r")

disegna_razzo()
sposta_stella()
aggiorna_hud()
loop_gioco()

schermo.mainloop()
