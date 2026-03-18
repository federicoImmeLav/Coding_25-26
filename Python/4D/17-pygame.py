import pygame

# comando che accende pygame
pygame.init()

# qui vanno invece tutte le cose per setuppare il gioco
# creo la schermata di gioco
schermo = pygame.display.set_mode((800,600))

# colori che mi servono nel gioco
rosso = (255,0,0) # codice RGB colore rosso
bianco = (255,255,255) # codice RGB bianco

# dimensione del quadrato
lato = 50

# posizione del quadrato
quad_x = 0
quad_y = 0

# variabile del gioco che è vera
gioco = True
while gioco:
    # fino a quando gioco non diventa falso, vai avanti
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
    # tutto quello che deve succedere nel gioco va qui:
    # impostiamo colore di sfondo bianco
    schermo.fill(bianco)

    # comando che avvisa pygame che premereo dei tasti
    tasto = pygame.key.get_pressed()

    # if che schiaccio i tasti e si muove
    if tasto[pygame.K_RIGHT]:
        quad_x += 1
    if tasto[pygame.K_LEFT]:
        quad_x -= 1
    if tasto[pygame.K_DOWN]:
        quad_y += 1
    if tasto [pygame.K_UP]:
        quad_y -= 1

    # comando per disegnare un quadrato
    pygame.draw.rect(schermo, rosso, (quad_x,quad_y,lato,lato))

    #comando che aggiorna lo schermo ogni volta
    pygame.display.update()

# comando di fine
pygame.quit()