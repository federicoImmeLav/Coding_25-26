import pygame
import random

# inizializzo pygame
pygame.init()

# impostazioni schermata
larghezza = 800
altezza = 600
schermo = pygame.display.set_mode((larghezza, altezza))
pygame.display.set_caption("Attraversa lo schermo")

# colori
bianco = (255,255,255)
rosso = (255,0,0)
verde = (0,255,0)
blu = (0,0,255)

# giocatore
player_x = 100
player_y = 300
player_dimensione = 50
player_velocità = 5
vite = 3

# ostacoli
ostacoli_fissi = [
    pygame.Rect(300, 100, 50, 50),
    pygame.Rect(500, 400, 50, 50)
]

ostacoli_mobili = [
    pygame.Rect(200, 0, 50, 50),
    pygame.Rect(600, 500, 50, 50)
]
ostacolo_mob_vel = [2, 3]  # velocità verticale ostacoli mobili

# orologio
clock = pygame.time.Clock()

# ciclo principale
gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

    # movimento giocatore
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_UP]:
        player_y -= player_velocità
    if tasti[pygame.K_DOWN]:
        player_y += player_velocità

    # limiti schermo
    if player_y < 0:
        player_y = 0
    if player_y > altezza - player_dimensione:
        player_y = altezza - player_dimensione

    # aggiornamento ostacoli mobili
    for i, ost in enumerate(ostacoli_mobili):
        ost.y += ostacolo_mob_vel[i]
        # rimbalzo tra bordo superiore e inferiore
        if ost.top <= 0 or ost.bottom >= altezza:
            ostacolo_mob_vel[i] *= -1

    # disegno sfondo
    schermo.fill(bianco)

    # disegno giocatore
    player_rect = pygame.Rect(player_x, player_y, player_dimensione, player_dimensione)
    pygame.draw.rect(schermo, rosso, player_rect)

    # disegno ostacoli fissi
    for ost in ostacoli_fissi:
        pygame.draw.rect(schermo, verde, ost)

    # disegno ostacoli mobili
    for ost in ostacoli_mobili:
        pygame.draw.rect(schermo, blu, ost)

    # controllo collisioni
    for ost in ostacoli_fissi + ostacoli_mobili:
        if player_rect.colliderect(ost):  # funzione pronta di pygame
            vite -= 1
            print(f"Hai perso una vita! Vite rimanenti: {vite}")
            # reset giocatore al centro verticale
            player_y = altezza // 2
            if vite == 0:
                print("Game Over!")
                gioco = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()