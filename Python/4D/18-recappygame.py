import pygame

# comando che accende pygame
pygame.init()

# creo la schermata di gioco
schermo = pygame.display.set_mode((600,400))

# scrivo caratteristiche del quadrato
quad_x = 0
quad_y = 0
lato = 50

# sezione dei colori
rosso = (255, 0, 0)
bianco = (255, 255, 255)

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
        quad_x += 1
    if tasto[pygame.K_LEFT]:
        quad_x -= 1
        
    # disegno il quadrato rosso
    pygame.draw.rect(schermo, rosso, (quad_x, quad_y, lato, lato))

    # funzione che aggiorna tutto
    pygame.display.update()

pygame.quit()

