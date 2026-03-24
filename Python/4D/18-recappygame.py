import pygame

# comando che accende pygame
pygame.init()

# creo la schermata di gioco
schermo = pygame.display.set_mode((600,400))

# scrivo caratteristiche del quadrato
quad_x = 0
quad_y = 0
lato = 50

# scrivo caratteristiche del cerchio
cer_x = 300
cer_y = 200
raggio = 20

# sezione dei colori
rosso = (255, 0, 0)
blu = (0, 0, 255)
bianco = (255, 255, 255)

# comando per fps
clock = pygame.time.Clock()

# creo variabile del gioco
gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
    # da qui in avanti si mette quello che fa il gioco
    # schermata bianca
    schermo.fill(bianco)

    # comando che vede che tasto premo
    tasto = pygame.key.get_pressed()
    if tasto[pygame.K_RIGHT]:
        quad_x += 5
    if tasto[pygame.K_LEFT]:
        quad_x -= 5
    if tasto[pygame.K_DOWN]:
        quad_y += 5
    if tasto[pygame.K_UP]:
        quad_y -= 5

    # faccio andare il cerchio verso il quadrato
    # se x cerchio è maggiore di x quadrato deve diminuire
    if cer_x > quad_x:
        cer_x -= 3
    elif cer_x < quad_x:
        cer_x += 3
    # vale anche per la y
    if cer_y > quad_y:
        cer_y -= 3
    elif cer_y < quad_y:
        cer_y += 3

    # misuro la distanza tra cerchio e quadrato
    dx = abs(cer_x - quad_x)
    dy = abs(cer_y - quad_y) 

    # se le distanza sono minori di 5 si ferma il gioco
    if dx < 5 and dy < 5:
        gioco = False  
    
    # disegno il quadrato rosso
    pygame.draw.rect(schermo, rosso, (quad_x, quad_y, lato, lato))
    # disegno il cerchio blu 
    pygame.draw.circle(schermo, blu, (cer_x, cer_y), raggio)

    # funzione che aggiorna tutto
    pygame.display.update()
    # imposto 60 fps
    clock.tick(60)

pygame.quit()

