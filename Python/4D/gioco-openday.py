import pygame
import random
import sys
import math

# ============================================================
#  🎮  CONFIGURA IL TUO PERSONAGGIO QUI SOTTO!
#  Cambia il nome e il colore prima di premere PLAY
# ============================================================

NOME_GIOCATORE = "Alessio"          # ← Scrivi il tuo nome tra le virgolette

# Scegli UN colore per il serpente (togli il # dal colore che vuoi):
#COLORE_SERPENTE = (34, 197, 94)      # Verde smeraldo  🟢
# COLORE_SERPENTE = (239, 68, 68)    # Rosso fuoco     🔴
# COLORE_SERPENTE = (59, 130, 246)   # Blu oceano      🔵
# COLORE_SERPENTE = (234, 179, 8)    # Giallo sole     🟡
# COLORE_SERPENTE = (168, 85, 247)   # Viola magico    🟣
# COLORE_SERPENTE = (249, 115, 22)   # Arancione       🟠
COLORE_SERPENTE = (236, 72, 153)   # Rosa shock      🩷
# COLORE_SERPENTE = (20, 184, 166)   # Turchese        🩵

# ============================================================
#  ⛔  NON MODIFICARE IL CODICE SOTTO QUESTA LINEA  ⛔
# ============================================================

pygame.init()
pygame.font.init()

# --- Costanti ---
LARGEZZA, ALTEZZA = 900, 700
CELLA = 30
COLS = (LARGEZZA - 200) // CELLA        # area di gioco: 700px
RIGHE = (ALTEZZA - 120) // CELLA        # area di gioco: 580px
OFS_X = 100                              # offset x area di gioco
OFS_Y = 80                               # offset y area di gioco
GAME_W = COLS * CELLA
GAME_H = RIGHE * CELLA
TEMPO_GIOCO = 20                         # secondi

NERO       = (10, 10, 15)
BIANCO     = (255, 255, 255)
SFONDO     = (15, 15, 25)
GRIGLIA    = (30, 30, 45)
ROSSO_MELA = (255, 60, 80)
GIALLO     = (255, 215, 0)
GRIGIO     = (80, 80, 100)
VERDE_HUD  = (100, 255, 150)

schermo = pygame.display.set_mode((LARGEZZA, ALTEZZA))
pygame.display.set_caption(f"🍎 Snake Open Day — {NOME_GIOCATORE}")
clock = pygame.time.Clock()

# Font
try:
    font_grande  = pygame.font.SysFont("segoeui",  52, bold=True)
    font_medio   = pygame.font.SysFont("segoeui",  28, bold=True)
    font_piccolo = pygame.font.SysFont("segoeui",  20)
    font_hud     = pygame.font.SysFont("couriernew", 22, bold=True)
except:
    font_grande  = pygame.font.Font(None, 64)
    font_medio   = pygame.font.Font(None, 36)
    font_piccolo = pygame.font.Font(None, 24)
    font_hud     = pygame.font.Font(None, 28)


def cella_a_pixel(cx, cy):
    return OFS_X + cx * CELLA, OFS_Y + cy * CELLA


def disegna_griglia():
    for x in range(COLS + 1):
        px = OFS_X + x * CELLA
        pygame.draw.line(schermo, GRIGLIA, (px, OFS_Y), (px, OFS_Y + GAME_H))
    for y in range(RIGHE + 1):
        py = OFS_Y + y * CELLA
        pygame.draw.line(schermo, GRIGLIA, (OFS_X, py), (OFS_X + GAME_W, py))


def disegna_bordo():
    rect = pygame.Rect(OFS_X - 3, OFS_Y - 3, GAME_W + 6, GAME_H + 6)
    pygame.draw.rect(schermo, COLORE_SERPENTE, rect, 3, border_radius=6)


def disegna_serpente(corpo):
    for i, (cx, cy) in enumerate(corpo):
        px, py = cella_a_pixel(cx, cy)
        colore = COLORE_SERPENTE
        # testa leggermente più chiara
        if i == 0:
            r = min(255, colore[0] + 60)
            g = min(255, colore[1] + 60)
            b = min(255, colore[2] + 60)
            colore = (r, g, b)
        rect = pygame.Rect(px + 2, py + 2, CELLA - 4, CELLA - 4)
        pygame.draw.rect(schermo, colore, rect, border_radius=7)
        # occhi sulla testa
        if i == 0:
            pygame.draw.circle(schermo, NERO, (px + 8, py + 8), 3)
            pygame.draw.circle(schermo, NERO, (px + CELLA - 8, py + 8), 3)


def disegna_mela(cx, cy, t):
    px, py = cella_a_pixel(cx, cy)
    bob = int(math.sin(t * 4) * 2)
    cx_m = px + CELLA // 2
    cy_m = py + CELLA // 2 + bob
    # corpo mela
    pygame.draw.circle(schermo, ROSSO_MELA, (cx_m, cy_m), CELLA // 2 - 4)
    # luccichio
    pygame.draw.circle(schermo, (255, 180, 180), (cx_m - 3, cy_m - 4), 3)
    # gambo
    pygame.draw.line(schermo, (100, 60, 20), (cx_m, cy_m - CELLA // 2 + 4),
                     (cx_m + 4, cy_m - CELLA // 2 - 2), 2)


def disegna_hud(punteggio, secondi_rimasti):
    # Barra superiore
    pygame.draw.rect(schermo, (20, 20, 35), (0, 0, LARGEZZA, OFS_Y - 5))
    
    # Nome giocatore
    txt = font_medio.render(f"👤  {NOME_GIOCATORE}", True, COLORE_SERPENTE)
    schermo.blit(txt, (OFS_X, 18))

    # Punteggio
    txt = font_medio.render(f"🍎  {punteggio}", True, GIALLO)
    schermo.blit(txt, (OFS_X + GAME_W // 2 - 40, 18))

    # Timer
    colore_timer = VERDE_HUD if secondi_rimasti > 8 else (
        GIALLO if secondi_rimasti > 4 else ROSSO_MELA)
    txt = font_medio.render(f"⏱  {secondi_rimasti}s", True, colore_timer)
    schermo.blit(txt, (OFS_X + GAME_W - 90, 18))

    # Barra timer visiva
    barra_w = int(GAME_W * (secondi_rimasti / TEMPO_GIOCO))
    pygame.draw.rect(schermo, GRIGLIA, (OFS_X, OFS_Y - 10, GAME_W, 6), border_radius=3)
    pygame.draw.rect(schermo, colore_timer, (OFS_X, OFS_Y - 10, barra_w, 6), border_radius=3)


def schermata_start():
    """Schermata iniziale con istruzioni."""
    t = 0
    while True:
        clock.tick(60)
        t += 0.016
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        schermo.fill(SFONDO)

        # Titolo animato
        scala = 1.0 + 0.03 * math.sin(t * 2)
        titolo = font_grande.render("🍎  SNAKE  OPEN DAY", True, COLORE_SERPENTE)
        w = int(titolo.get_width() * scala)
        h = int(titolo.get_height() * scala)
        titolo_scaled = pygame.transform.scale(titolo, (w, h))
        schermo.blit(titolo_scaled, (LARGEZZA // 2 - w // 2, 90))

        # Info giocatore
        txt = font_medio.render(f"Benvenuto/a,  {NOME_GIOCATORE}!", True, BIANCO)
        schermo.blit(txt, (LARGEZZA // 2 - txt.get_width() // 2, 200))

        # Quadratino colore serpente
        pygame.draw.rect(schermo, COLORE_SERPENTE,
                         (LARGEZZA // 2 - 15, 245, 30, 30), border_radius=5)
        txt2 = font_piccolo.render("← il tuo serpente", True, GRIGIO)
        schermo.blit(txt2, (LARGEZZA // 2 + 20, 250))

        # Istruzioni
        istruzioni = [
            "Usa le  ↑ ↓ ← →  per muovere il serpente",
            f"Raccogli più mele che puoi in  {TEMPO_GIOCO}  secondi!",
            "Attenzione: non uscire dai bordi!",
        ]
        y = 310
        for riga in istruzioni:
            t_riga = font_piccolo.render(riga, True, (180, 180, 210))
            schermo.blit(t_riga, (LARGEZZA // 2 - t_riga.get_width() // 2, y))
            y += 36

        # PLAY button pulsante
        alfa = int(180 + 75 * math.sin(t * 3))
        colore_btn = (min(255, COLORE_SERPENTE[0] + 20),
                      min(255, COLORE_SERPENTE[1] + 20),
                      min(255, COLORE_SERPENTE[2] + 20))
        pygame.draw.rect(schermo, colore_btn,
                         (LARGEZZA // 2 - 120, 460, 240, 60), border_radius=12)
        play_txt = font_medio.render("▶   PREMI SPAZIO", True, NERO)
        schermo.blit(play_txt, (LARGEZZA // 2 - play_txt.get_width() // 2, 476))

        pygame.display.flip()


def schermata_game_over(punteggio, record):
    """Schermata fine gioco con punteggio."""
    t = 0
    while True:
        clock.tick(60)
        t += 0.016
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True   # rigioca
                if event.key == pygame.K_ESCAPE:
                    return False  # esci

        schermo.fill(SFONDO)

        # Titolo
        txt = font_grande.render("⏰  TEMPO SCADUTO!", True, ROSSO_MELA)
        schermo.blit(txt, (LARGEZZA // 2 - txt.get_width() // 2, 80))

        # Nome
        txt = font_medio.render(f"{NOME_GIOCATORE}", True, COLORE_SERPENTE)
        schermo.blit(txt, (LARGEZZA // 2 - txt.get_width() // 2, 180))

        # Punteggio grande
        num = font_grande.render(str(punteggio), True, GIALLO)
        schermo.blit(num, (LARGEZZA // 2 - num.get_width() // 2, 240))
        etichetta = font_piccolo.render("mele raccolte", True, GRIGIO)
        schermo.blit(etichetta, (LARGEZZA // 2 - etichetta.get_width() // 2, 320))

        # Record
        if punteggio >= record:
            rec_txt = font_medio.render("🏆  NUOVO RECORD!", True, GIALLO)
        else:
            rec_txt = font_medio.render(f"Record:  {record}  mele", True, GRIGIO)
        schermo.blit(rec_txt, (LARGEZZA // 2 - rec_txt.get_width() // 2, 380))

        # Pulsanti
        scala = 1.0 + 0.02 * math.sin(t * 3)
        pygame.draw.rect(schermo, COLORE_SERPENTE,
                         (LARGEZZA // 2 - 140, 460, 280, 55), border_radius=12)
        r_txt = font_medio.render("▶   SPAZIO = rigioca", True, NERO)
        schermo.blit(r_txt, (LARGEZZA // 2 - r_txt.get_width() // 2, 474))

        esc_txt = font_piccolo.render("ESC = esci", True, GRIGIO)
        schermo.blit(esc_txt, (LARGEZZA // 2 - esc_txt.get_width() // 2, 535))

        pygame.display.flip()


def nuova_mela(corpo):
    while True:
        cx = random.randint(0, COLS - 1)
        cy = random.randint(0, RIGHE - 1)
        if (cx, cy) not in corpo:
            return cx, cy


def gioca():
    """Loop principale del gioco. Restituisce il punteggio."""
    corpo = [(COLS // 2, RIGHE // 2),
             (COLS // 2 - 1, RIGHE // 2),
             (COLS // 2 - 2, RIGHE // 2)]
    direzione = (1, 0)
    prossima_dir = (1, 0)
    mela = nuova_mela(corpo)
    punteggio = 0
    t_inizio = pygame.time.get_ticks()
    t_animazione = 0.0
    velocita = 8  # mosse al secondo
    t_ultima_mossa = pygame.time.get_ticks()

    while True:
        clock.tick(60)
        t_animazione += 0.016
        adesso = pygame.time.get_ticks()
        secondi_rimasti = max(0, TEMPO_GIOCO - (adesso - t_inizio) // 1000)

        # Gestione input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP    and direzione != (0, 1):
                    prossima_dir = (0, -1)
                if event.key == pygame.K_DOWN  and direzione != (0, -1):
                    prossima_dir = (0, 1)
                if event.key == pygame.K_LEFT  and direzione != (1, 0):
                    prossima_dir = (-1, 0)
                if event.key == pygame.K_RIGHT and direzione != (-1, 0):
                    prossima_dir = (1, 0)

        # Movimento
        intervallo = 1000 // velocita
        if adesso - t_ultima_mossa >= intervallo:
            t_ultima_mossa = adesso
            direzione = prossima_dir
            testa = corpo[0]
            nuova_testa = (testa[0] + direzione[0], testa[1] + direzione[1])

            # Collisione bordo → fine
            if not (0 <= nuova_testa[0] < COLS and 0 <= nuova_testa[1] < RIGHE):
                return punteggio
            # Collisione sé stesso → fine
            if nuova_testa in corpo:
                return punteggio

            corpo.insert(0, nuova_testa)

            if nuova_testa == mela:
                punteggio += 1
                mela = nuova_mela(corpo)
                # Aumenta velocità ogni 3 mele
                velocita = 8 + punteggio // 3
            else:
                corpo.pop()

        # Fine per timeout
        if secondi_rimasti == 0:
            return punteggio

        # --- Disegno ---
        schermo.fill(SFONDO)
        disegna_griglia()
        disegna_bordo()
        disegna_mela(*mela, t_animazione)
        disegna_serpente(corpo)
        disegna_hud(punteggio, secondi_rimasti)
        pygame.display.flip()


def main():
    record = 0
    schermata_start()
    while True:
        punteggio = gioca()
        record = max(record, punteggio)
        rigioca = schermata_game_over(punteggio, record)
        if not rigioca:
            break
    pygame.quit()


if __name__ == "__main__":
    main()