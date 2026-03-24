import pygame
import random

# accendo pygame
pygame.init()

# schermata
larghezza = 800
altezza = 600
schermo = pygame.display.set_mode((larghezza, altezza))

# creo i colori
bianco = (255,255,255)
rosso = (255,0,0)
blu = (0,0,255)
nero = (0,0,0)

# caratteristiche del quadrato
quad_x = larghezza / 2
quad_y = altezza - 100
lato = 50
quad_vel = 5

# caratteristiche del cerchio
cer_x = random.randint(10 , larghezza-50)
cer_y = -20
raggio = 20
cer_vel = 3

clock = pygame.time.Clock()
# inizio del gioco
gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
    schermo.fill(bianco)

    # imposto cerchio che precipita
    cer_y += cer_vel
    # faccio tornare il cerchio su in un posto casuale quando tocca il bordo giu
    if cer_y > altezza:
        cer_y = -20
        cer_x = random.randint(10 , larghezza-50)

    # comando per muovere il quadrato
    # si muove solo in orizzontale e non può uscire dai bordi
    tasto = pygame.key.get_pressed()
    if tasto[pygame.K_LEFT]:
        quad_x -= quad_vel
    if tasto[pygame.K_RIGHT]:
        quad_x += quad_vel

    # misuro la distanza tra cerchio e quadrato
    centro_x = quad_x + lato / 2
    centro_y = quad_y + lato / 2
    
    dx = abs(cer_x - centro_x)
    dy = abs(cer_y - centro_y) 

    if dx < 30 and dy < 30:
        cer_y = -20
        cer_x = random.randint(10 , larghezza-50)

    # disegno quadrato
    pygame.draw.rect(schermo, rosso,(quad_x, quad_y, lato, lato))
    # disegno cerchio
    pygame.draw.circle(schermo, blu, (cer_x, cer_y), raggio)

    # aggiorno il gioco
    pygame.display.update()
    clock.tick(60)

# fine del gioco
pygame.quit()