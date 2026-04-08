import pygame
import random

# Inizializzazione
pygame.init()
LARGHEZZA, ALTEZZA = 300, 600
DIM_CELLA = 30
COLONNE, RIGHE = LARGHEZZA // DIM_CELLA, ALTEZZA // DIM_CELLA
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))

# Colori (RGB)
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
COLORI_PEZZI = [(0, 255, 255), (255, 165, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (128, 0, 128), (255, 0, 0)]

# Forme dei pezzi (Matrici 0/1)
FORME = [
    [[1, 1, 1, 1]], # I
    [[1, 1, 1], [0, 1, 0]], # T
    [[1, 1], [1, 1]], # O
    [[0, 1, 1], [1, 1, 0]], # S
    [[1, 1, 0], [0, 1, 1]]  # Z
]

class Pezzo:
    def __init__(self):
        self.forma = random.choice(FORME)
        self.colore = random.choice(COLORI_PEZZI)
        self.x = COLONNE // 2 - len(self.forma[0]) // 2
        self.y = 0

    def ruota(self):
        self.forma = [list(r) for r in zip(*self.forma[::-1])]

def check_collisione(griglia, pezzo, dx=0, dy=0, nuova_forma=None):
    forma = nuova_forma or pezzo.forma
    for r, riga in enumerate(forma):
        for c, valore in enumerate(riga):
            if valore:
                nuova_x, nuova_y = pezzo.x + c + dx, pezzo.y + r + dy
                if nuova_x < 0 or nuova_x >= COLONNE or nuova_y >= RIGHE or \
                   (nuova_y >= 0 and griglia[nuova_y][nuova_x]):
                    return True
    return False

def cancella_righe(griglia):
    nuova_griglia = [riga for riga in griglia if any(valore == 0 for valore in riga)]
    righe_eliminate = RIGHE - len(nuova_griglia)
    return [[0 for _ in range(COLONNE)] for _ in range(righe_eliminate)] + nuova_griglia

# Gioco principale
griglia = [[0 for _ in range(COLONNE)] for _ in range(RIGHE)]
pezzo_attuale = Pezzo()
clock = pygame.time.Clock()
timer_caduta = 0

running = True
while running:
    schermo.fill(NERO)
    timer_caduta += clock.get_rawtime()
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not check_collisione(griglia, pezzo_attuale, dx=-1):
                pezzo_attuale.x -= 1
            if event.key == pygame.K_RIGHT and not check_collisione(griglia, pezzo_attuale, dx=1):
                pezzo_attuale.x += 1
            if event.key == pygame.K_DOWN and not check_collisione(griglia, pezzo_attuale, dy=1):
                pezzo_attuale.y += 1
            if event.key == pygame.K_UP:
                ruotato = [list(r) for r in zip(*pezzo_attuale.forma[::-1])]
                if not check_collisione(griglia, pezzo_attuale, nuova_forma=ruotato):
                    pezzo_attuale.ruota()

    # Logica caduta automatica
    if timer_caduta > 500: # 500ms
        if not check_collisione(griglia, pezzo_attuale, dy=1):
            pezzo_attuale.y += 1
        else:
            # Blocca il pezzo nella griglia
            for r, riga in enumerate(pezzo_attuale.forma):
                for c, valore in enumerate(riga):
                    if valore: griglia[pezzo_attuale.y + r][pezzo_attuale.x + c] = pezzo_attuale.colore
            griglia = cancella_righe(griglia)
            pezzo_attuale = Pezzo()
            if check_collisione(griglia, pezzo_attuale): running = False # Game Over
        timer_caduta = 0

    # Disegno griglia e pezzo
    for y, riga in enumerate(griglia):
        for x, valore in enumerate(riga):
            if valore: pygame.draw.rect(schermo, valore, (x*DIM_CELLA, y*DIM_CELLA, DIM_CELLA-1, DIM_CELLA-1))
    
    for r, riga in enumerate(pezzo_attuale.forma):
        for c, valore in enumerate(riga):
            if valore: pygame.draw.rect(schermo, pezzo_attuale.colore, ((pezzo_attuale.x + c)*DIM_CELLA, (pezzo_attuale.y + r)*DIM_CELLA, DIM_CELLA-1, DIM_CELLA-1))

    pygame.display.flip()

pygame.quit()