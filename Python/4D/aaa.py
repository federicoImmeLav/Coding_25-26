import pygame
import random

# comando che accende pygame
pygame.init()

# creo la schermata di gioco
schermo = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Clicca sui bersagli")

# caratteristiche del bersaglio
bers_x = random.randint(0, 560)
bers_y = random.randint(60, 500)
lato = 40

# sezione dei colori
rosso = (220, 50, 50)
nero = (0, 0, 0)
bianco = (255, 255, 255)
grigio = (180, 180, 180)

# font per il testo
font = pygame.font.SysFont("Arial", 24)

# variabili di gioco
punti = 0
tempo = 10

# comando per fps
clock = pygame.time.Clock()

# timer: evento custom ogni 1000ms
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000)

# creo variabile del gioco
gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

        # ogni secondo diminuisce il timer
        if evento.type == TIMER_EVENT:
            tempo -= 1
            if tempo <= 0:
                gioco = False

        # controllo il click del mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evento.pos
            if bers_x < mx < bers_x + lato and bers_y < my < bers_y + lato:
                punti += 1
                bers_x = random.randint(0, 560)
                bers_y = random.randint(60, 500)

    # schermata bianca
    schermo.fill(bianco)

    # disegno il bersaglio
    pygame.draw.rect(schermo, rosso, (bers_x, bers_y, lato, lato))

    # scrivo punti e timer
    schermo.blit(font.render(f"Punti: {punti}", True, nero), (20, 15))
    schermo.blit(font.render(f"Timer: {tempo}", True, nero), (440, 15))

    # scrivo le istruzioni in basso
    istr = font.render("Clicca sui bersagli!", True, grigio)
    schermo.blit(istr, (300 - istr.get_width() // 2, 560))

    # funzione che aggiorna tutto
    pygame.display.update()
    # imposto 60 fps
    clock.tick(60)

# schermata finale
schermo.fill(bianco)
msg = font.render(f"Tempo scaduto! Hai fatto {punti} punti", True, nero)
schermo.blit(msg, (300 - msg.get_width() // 2, 280))
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()