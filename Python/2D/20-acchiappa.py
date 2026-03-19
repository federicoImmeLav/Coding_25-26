import pygame
import random

# accendo pygame
pygame.init()

# creo schermata di gioco
schermo = pygame.display.set_mode((800,600))

# creo i colori per il gioco
bianco = (255,255,255)
rosso = (255,0,0)
blu = (0,0,255)

# imposto le caratteristiche del quadrato (pg)
quad_x = 400
quad_y = 500
lato = 50
quad_vel = 5

# caratteristiche del cerchio
cer_x = random.randint(20,780)
cer_y = -20 # compare da sopra lo schermo
raggio = 20
cer_vel = 4

# creo variabile punteggio
punteggio = 0

# imposto il carattere per scrivere
testo = pygame.font.SysFont("Arial", 30)

# comando per limitare gli fps
clock = pygame.time.Clock()

# creo il loop del gioco (while)
gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
    
    # schermata bianca
    schermo.fill(bianco)

    # attivo i tasti
    tasto = pygame.key.get_pressed()
    if tasto[pygame.K_RIGHT]:
        quad_x += quad_vel
    if tasto[pygame.K_LEFT]:
        quad_x -= quad_vel

    # evito che il quadrato esca dalla schermata
    if quad_x < 0:
        quad_x = 0
    if quad_x > 800 - lato:
        quad_x = 800 - lato

    # comando che fa cadere il cerchio
    cer_y += cer_vel
    
    # se il cerchio supera il bordo sotto, ricompare sopra
    if cer_y > 600:
        cer_x = random.randint(20,780)
        cer_y = -20

    # collisione tra cerchio e quadrato
    # calcolo il centro del quadrato
    centro_x = quad_x + lato / 2
    centro_y = quad_y + lato / 2

    # misuro la distanza tra quadrato e cerchio
    dx = abs(cer_x - centro_x)
    dy = abs(cer_y - centro_y)

    # se dx e dy sono minori di 5 si toccano
    if dx < 40 and dy < 40: 
        cer_x = random.randint(20,780)
        cer_y = -20
        punteggio += 1

    # disegno il quadrato 
    pygame.draw.rect(schermo, rosso, (quad_x,quad_y, lato, lato))
    # disegno il cerchio
    pygame.draw.circle(schermo, blu, (cer_x,cer_y), raggio)

    # disegno sullo schermo la scritta
    punti = testo.render(f"Punteggio: {punteggio} ", True, rosso)
    schermo.blit(punti, (30,30))

    # aggiorno lo schermo ad ogni loop
    pygame.display.update()
    clock.tick(60)

pygame.quit()