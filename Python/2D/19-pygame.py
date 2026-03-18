# importo le librerie che ci servono
import pygame
import random

# comando che accende pygame
pygame.init()

# creo la schermata di gioco
schermo = pygame.display.set_mode((800,600))

# Cose per setuppare il gioco
bianco = (255,255,255)
rosso = (255,0,0)
verde = (0,255,0)

# Posizione di spawn del quadrato
x = 0
y = 0

# Spawn del cerchio
cerchio_x = 500
cerchio_y = 300

# raggio del cerchio
raggio = 20

# dimensione del quadrato
dimensione = 50

# creo orologio per aggiornamento del while
clock = pygame.time.Clock()

# ciclo che va avanti all'infinito fino a quando non lo stoppo
gioco = True

while gioco:
    for evento in pygame.event.get():
        if evento.type  == pygame.QUIT:
            gioco = False
    # comando per colorare lo sfondo
    schermo.fill(bianco)

    # controllo che i tasti vengano premuti
    tasti = pygame.key.get_pressed()
    # if per muovermi
    if tasti[pygame.K_DOWN]:
        y += 5
    if tasti[pygame.K_UP]:
        y -= 5
    if tasti[pygame.K_RIGHT]:
        x += 5
    if tasti[pygame.K_LEFT]:
        x -= 5

    # considero il centro del quadrato
    quadr_x = x + dimensione / 2
    quadr_y = y + dimensione / 2
    
    # controllo la posizione del cerchio e lo avvicino al quadrato
    vel_cerchio = 2
    if cerchio_x > quadr_x:
        cerchio_x -= vel_cerchio
    if cerchio_x < quadr_x:
        cerchio_x += vel_cerchio
    if cerchio_y > quadr_y:
        cerchio_y -= vel_cerchio
    if cerchio_y < quadr_y:
        cerchio_y += vel_cerchio

    # calcolo la distanza x e y tra cerchio e quadrato 
    # togliendo il segno (valore assoluto) (abs)
    dx = abs(cerchio_x - quadr_x)
    dy = abs(cerchio_y - quadr_y)
    if dx < 5 and dy < 5:
        gioco = False

    # disegno il quadrato
    pygame.draw.rect(schermo, rosso, (x,y, dimensione,dimensione))

    # disegno il cerchio
    pygame.draw.circle(schermo, verde, (cerchio_x, cerchio_y), raggio)

    # aggiorno lo schermo alla fine di ogni ciclo
    pygame.display.update()

    # mettiamo la frequenza di aggiornamento del while
    clock.tick(60)

pygame.quit()