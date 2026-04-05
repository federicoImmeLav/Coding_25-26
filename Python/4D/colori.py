import pygame
import random

pygame.init()

schermo = pygame.display.set_mode((600, 600))

bianco = (255, 255, 255)
nero = (0, 0, 0)

# dizionario: nome colore -> valore RGB
colori = {
    "ROSSO": (220, 50, 50),
    "VERDE": (50, 180, 50),
    "BLU": (50, 100, 220)
}
nomi = list(colori.keys())

def nuova_domanda():
    # scelgo quale colore cliccare
    target = random.choice(nomi)

    # scelgo 3 colori distinti da mostrare come quadrati
    quadrati = random.sample(nomi, 3)

    # scelgo un colore diverso da target per colorare la scritta
    altri_colori = [n for n in nomi if n != target]
    colore_scritta = random.choice(altri_colori)

    return target, quadrati, colore_scritta

testo_grande = pygame.font.SysFont("Arial", 36, bold=True)
testo_piccolo = pygame.font.SysFont("Arial", 20)

punti = 0
tempo = 30
target, quadrati, colore_scritta = nuova_domanda()

# posizioni fisse dei 3 quadrati in fila
lato = 100
posizioni = [(100, 350), (250, 350), (400, 350)]

clock = pygame.time.Clock()
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 1000)

gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

        if evento.type == TIMER:
            tempo -= 1
            if tempo == 0:
                gioco = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            for i, (qx, qy) in enumerate(posizioni):
                if qx < x < qx + lato and qy < y < qy + lato:
                    if quadrati[i] == target:
                        punti += 1
                    else:
                        punti -= 1
                    target, quadrati, colore_scritta = nuova_domanda()
                    break

    schermo.fill(bianco)

    # scrivo "Clicca:" in nero e poi il nome del colore nel colore sbagliato
    scrivi = testo_grande.render("Clicca:", True, nero)
    scrivi_colore = testo_grande.render(target, True, colori[colore_scritta])
    schermo.blit(scrivi, (150, 200))
    schermo.blit(scrivi_colore, (300, 200))

    # disegno i 3 quadrati
    for i, (qx, qy) in enumerate(posizioni):
        pygame.draw.rect(schermo, colori[quadrati[i]], (qx, qy, lato, lato))

    # punteggio e tempo
    schermo.blit(testo_piccolo.render(f"Punteggio: {punti}", True, nero), (20, 15))
    schermo.blit(testo_piccolo.render(f"Tempo: {tempo}", True, nero), (480, 15))

    pygame.display.update()
    clock.tick(60)

# schermata finale
schermo.fill(bianco)
schermo.blit(testo_grande.render(f"Hai fatto: {punti} punti", True, nero), (180, 280))
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()