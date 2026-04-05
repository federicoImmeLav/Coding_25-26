import pygame
import random

pygame.init()

# schermata di gioco
schermo = pygame.display.set_mode((600,600))

# definisco i colori del gioco
bianco = (255,255,255)
rosso = (255,0,0)
nero = (0,0,0)
verde = (0,255,0)
blu = (0,0,255)

colori = [rosso, nero, verde, blu]
colore = random.choice(colori)

# caratteristiche del quadrato
lato = 40
quad_x = random.randint(0, 560)
quad_y = random.randint(60,500)

# definisco proprietà della scritta
testo = pygame.font.SysFont("Arial", 20)

# creo punti e tempo
punti = 0
tempo = 5

# controllo degli fps
clock = pygame.time.Clock()

# creo un evento che si ripete ogni secondo
TIMER = pygame.USEREVENT + 1
# dico all'evento di ripetersi ogni secondo
pygame.time.set_timer(TIMER, 1000)

gioco = True
while gioco: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
        # evento del tempo che passa, c'è un evento che ripete ogni volta che gli diciamo
        # noi quanto aspettare 
        if evento.type == TIMER:
            tempo -= 1
            if tempo == 0:
                gioco = False

        # controllo un evento che clicca il mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x,y = evento.pos 
            print(x,y)
            if quad_x < x < quad_x + 40 and quad_y < y < quad_y + 40:
                quad_x = random.randint(0, 560)
                quad_y = random.randint(60, 500)
                colore = random.choice(colori)
                # aumento i punti
                punti += 1
            else:
                # perdo punti solo se clicco nel posto sbagliato
                punti -= 1

            # dopo che clicco, controllo quale clicco
            # if evento.button == 1:
            #     quad_x = random.randint(0, 560)
            #     quad_y = random.randint(60, 500)

    schermo.fill(bianco)

    # disegno quadrato
    pygame.draw.rect(schermo, colore, (quad_x, quad_y, lato, lato))
    # inserisco una scritta
    schermo.blit(testo.render(f"Punteggio: {punti}", True, nero), (20,15))
    schermo.blit(testo.render(f"Tempo: {tempo}", True, nero), (400,15))

    pygame.display.update()

# schermata bianca con scritta del punteggio quando finisce il tempo
schermo.fill(bianco)
schermo.blit(testo.render(f"Hai fatto: {punti} punti", True, nero), (300,300))
pygame.display.update()
# aspetto 3 s prima di chiudere
pygame.time.wait(3000)

pygame.quit()