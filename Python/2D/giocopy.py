
import pygame
import random
import sys

# ============= INIZIALIZZAZIONE =============

pygame.init()

# Dimensioni dello schermo
LARGHEZZA, ALTEZZA = 800, 600

# Crea la finestra
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Evita gli Ostacoli!")

# Clock per controllare i FPS (fotogrammi al secondo)
clock = pygame.time.Clock()

# Font per disegnare il testo
font = pygame.font.Font(None, 36)

# ============= COLORI (RGB) =============

BIANCO = (255, 255, 255)    # Sfondo
NERO = (0, 0, 0)            # Testo
ROSSO = (255, 0, 0)         # Nemici
BLU = (0, 0, 255)           # Player
VERDE = (0, 255, 0)         # Non usato in questo gioco, ma potrebbe servire

# ============= PLAYER =============

# Crea il player (quadratino blu) al centro-basso dello schermo
player = pygame.Rect(LARGHEZZA // 2, ALTEZZA - 50, 50, 50)

# Quanto velocemente il player si muove
player_velocita = 5

# ============= NEMICI =============

# Lista vuota che conterrà tutti i nemici
nemici = []

# Punteggio iniziale
score = 0

# ============= GAME LOOP =============

running = True

while running:
    
    # Mantieni il gioco a 60 FPS
    clock.tick(60)
    
    # ===== EVENT HANDLING =====
    # Cattura gli input dell'utente
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # ===== INPUT DA TASTIERA =====
    # Movimento del player con frecce sinistra e destra
    
    keys = pygame.key.get_pressed()
    
    # Freccia sinistra: muovi il player a sinistra
    # Controlla che non esca dal bordo sinistro
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_velocita
    
    # Freccia destra: muovi il player a destra
    # Controlla che non esca dal bordo destro
    if keys[pygame.K_RIGHT] and player.x < LARGHEZZA - player.width:
        player.x += player_velocita
    
    # ===== CREAZIONE NEMICI =====
    # Crea nemici casuali dall'alto
    
    # Massimo 5 nemici contemporaneamente per non rendere troppo difficile
    if len(nemici) < 5:
        
        # 3% di probabilità di creare un nemico ogni frame
        if random.randint(0, 100) < 3:
            
            # Posizione orizzontale casuale
            x_nemico = random.randint(0, LARGHEZZA - 40)
            
            # Crea il nemico sopra lo schermo (y = -40)
            nemico = pygame.Rect(x_nemico, -40, 40, 40)
            
            # Aggiungi il nemico alla lista
            nemici.append(nemico)
    
    # ===== MOVIMENTO NEMICI =====
    # Muovi i nemici verso il basso
    
    for nemico in nemici:
        nemico.y += 3  # Velocità di movimento (pixel per frame)
    
    # ===== PULIZIA NEMICI =====
    # Rimuovi i nemici che sono usciti dal basso dello schermo
    
    nemici = [n for n in nemici if n.y < ALTEZZA]
    
    # ===== COLLISIONI =====
    # Controlla se il player tocca un nemico
    
    game_over = False
    
    for nemico in nemici:
        # colliderect() ritorna True se due rettangoli si toccano
        if player.colliderect(nemico):
            game_over = True
            break
    
    # Se c'è stata una collisione, termina il gioco
    if game_over:
        running = False
    
    # ===== PUNTEGGIO =====
    # Aumenta il punteggio ogni frame (se il gioco non è finito)
    
    if not game_over:
        score += 1
    
    # ===== DISEGNO =====
    # Disegna tutto sullo schermo
    
    # Colora lo schermo di bianco
    schermo.fill(BIANCO)
    
    # Disegna il player (quadratino blu)
    pygame.draw.rect(schermo, BLU, player)
    
    # Disegna tutti i nemici (quadratini rossi)
    for nemico in nemici:
        pygame.draw.rect(schermo, ROSSO, nemico)
    
    # ===== TESTO =====
    # Disegna il punteggio sullo schermo
    
    # Dividiamo score per 60 per avere il tempo in secondi
    # (il gioco gira a 60 FPS, quindi 60 frame = 1 secondo)
    score_text = font.render(f"Score: {score // 60}", True, NERO)
    
    # Disegna il testo nelle coordinate (10, 10)
    schermo.blit(score_text, (10, 10))
    
    # ===== AGGIORNA DISPLAY =====
    # Mostra tutto quello che abbiamo disegnato
    
    pygame.display.flip()

# Quando il gioco finisce, chiudi pygame
pygame.quit()
