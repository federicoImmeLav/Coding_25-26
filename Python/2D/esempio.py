# ============================================================
#  ACCHIAPPA I CERCHI  🎮
#  Muovi il quadrato con le frecce e prendi i cerchi che cadono!
# ============================================================

# --- STEP 1: importo le librerie ---
import pygame
import random

# --- STEP 2: accendo pygame ---
pygame.init()

# --- STEP 3: creo la schermata ---
LARGHEZZA = 800
ALTEZZA   = 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Acchiappa i Cerchi!")

# --- STEP 4: colori (rosso, verde, blu) da 0 a 255 ---
BIANCO  = (255, 255, 255)
ROSSO   = (220,  50,  50)
BLU     = ( 50, 100, 220)
GIALLO  = (255, 220,   0)
GRIGIO  = (180, 180, 180)
NERO    = (  0,   0,   0)

# --- STEP 5: variabili del quadrato (il giocatore) ---
quadrato_x    = LARGHEZZA // 2   # parte al centro dello schermo
quadrato_y    = ALTEZZA - 80     # parte in basso
dimensione    = 50               # lato del quadrato in pixel
velocita_quad = 6                # pixel che si muove per ogni frame

# --- STEP 6: variabili del PRIMO cerchio ---
#   ogni cerchio ha: posizione x, posizione y, velocità di caduta
cerchio_x  = random.randint(20, LARGHEZZA - 20)   # colonna casuale
cerchio_y  = -20                                   # parte sopra lo schermo
raggio     = 20                                    # raggio in pixel
velocita_c = 4                                     # pixel che scende per frame

# --- STEP 7: punteggio ---
punteggio = 0

# --- STEP 8: font per scrivere il punteggio a schermo ---
font_grande  = pygame.font.SysFont("Arial", 36)
font_piccolo = pygame.font.SysFont("Arial", 24)

# --- STEP 9: orologio per bloccare il gioco a 60 fps ---
clock = pygame.time.Clock()

# --- STEP 10: variabile che tiene vivo il ciclo ---
gioco = True

# ============================================================
#  CICLO PRINCIPALE  (uguale a prima, gira 60 volte al secondo)
# ============================================================
while gioco:

    # -- GESTIONE EVENTI (chiudi finestra) --
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

    # -- SFONDO --
    schermo.fill(BIANCO)

    # --------------------------------------------------------
    #  MOVIMENTO DEL QUADRATO con le frecce
    # --------------------------------------------------------
    tasti = pygame.key.get_pressed()

    if tasti[pygame.K_LEFT]:
        quadrato_x -= velocita_quad
    if tasti[pygame.K_RIGHT]:
        quadrato_x += velocita_quad

    # blocco il quadrato ai bordi dello schermo (non esce fuori)
    if quadrato_x < 0:
        quadrato_x = 0
    if quadrato_x + dimensione > LARGHEZZA:
        quadrato_x = LARGHEZZA - dimensione

    # --------------------------------------------------------
    #  CADUTA DEL CERCHIO
    #  ogni frame lo sposto un po' più in basso
    # --------------------------------------------------------
    cerchio_y += velocita_c

    # se il cerchio esce dal basso senza essere preso → lo rispawno in alto
    if cerchio_y - raggio > ALTEZZA:
        cerchio_x = random.randint(raggio, LARGHEZZA - raggio)
        cerchio_y = -raggio   # riparte da sopra

    # --------------------------------------------------------
    #  RILEVAMENTO COLLISIONE
    #  uso il centro del quadrato e calcolo la distanza dal cerchio
    #  (stessa tecnica del codice originale con dx e dy)
    # --------------------------------------------------------
    centro_quad_x = quadrato_x + dimensione / 2
    centro_quad_y = quadrato_y + dimensione / 2

    dx = abs(cerchio_x - centro_quad_x)
    dy = abs(cerchio_y - centro_quad_y)

    # la collisione avviene quando cerchio e quadrato si sovrappongono
    # uso il raggio + metà del lato come soglia di contatto
    soglia = raggio + dimensione / 2

    if dx < soglia and dy < soglia:
        # HO PRESO IL CERCHIO!
        punteggio += 1

        # il cerchio respawna in cima con colonna casuale
        cerchio_x = random.randint(raggio, LARGHEZZA - raggio)
        cerchio_y = -raggio

        # ogni 5 punti il cerchio va un po' più veloce (difficoltà crescente)
        if punteggio % 5 == 0:
            velocita_c += 1

    # --------------------------------------------------------
    #  DISEGNO  (prima il quadrato, poi il cerchio, poi il testo)
    # --------------------------------------------------------

    # disegno il quadrato (il giocatore)
    pygame.draw.rect(schermo, ROSSO, (quadrato_x, quadrato_y, dimensione, dimensione))

    # disegno il cerchio (che cade)
    pygame.draw.circle(schermo, BLU, (cerchio_x, cerchio_y), raggio)

    # disegno il punteggio in alto a sinistra
    testo_punteggio = font_grande.render("Punti: " + str(punteggio), True, NERO)
    schermo.blit(testo_punteggio, (20, 20))

    # piccolo suggerimento in basso
    testo_aiuto = font_piccolo.render("Frecce ← → per muoverti", True, GRIGIO)
    schermo.blit(testo_aiuto, (20, ALTEZZA - 35))

    # --------------------------------------------------------
    #  AGGIORNO LO SCHERMO e aspetto il prossimo frame
    # --------------------------------------------------------
    pygame.display.update()
    clock.tick(60)

# -- Fine del ciclo: chiudo pygame --
pygame.quit()
