import pygame
import random

# accendo pygame
pygame.init()

# creazione della schermata
larghezza = 600
altezza = 600
schermo = pygame.display.set_mode((larghezza,altezza))

# qui si definisco colori, dimensioni, posizioni, etc
# creo il bianco
bianco = (255,255,255)
# creo il rosso
rosso = (255, 0, 0)
# definire le coordinate del quadrato
x_quad = 200
y_quad = 400
# definisco il lato del quadrato
lato = 50

# definisco coordinate del cerchio
x_cer = 300
y_cer = 150
# raggio del cerchio
raggio = 20


# creo il loop del gioco, che è un while che fa funzionare tutto
# fino a quando non si decide che deve spegnersi
gioco = True
while gioco: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
    # imposto il colore dello sfondo
    schermo.fill(bianco)

    # disegna il quadrato
    pygame.draw.rect(schermo, rosso, (x_quad, y_quad, lato,lato))
    # disegno il cerchi
    pygame.draw.circle(schermo, rosso, (x_cer,y_cer), raggio)
    # aggiorno tutto quello che succede prima
    pygame.display.update()

pygame.quit()