import pygame
import player
pygame.init()

clock = pygame.time.Clock()

background = pygame.image.load("background.png")

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dracarys")

Drogo = player.Player(win, SCREEN_WIDTH, SCREEN_HEIGHT)

#TEMPORARY FOR DEBUGGING
Boat = player.Boat(win, SCREEN_WIDTH, SCREEN_HEIGHT)


gameon = True
while gameon:

    clock.tick(60)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            gameon = False
    win.blit(background, (0,0))
    
    collision = Drogo.collision()
    Drogo.movement(collision)
    Drogo.draw()
    Drogo.attack()

    #TEMPORARY FOR DEBUGGING
    Boat.movement(Drogo.x)
    Boat.draw()
    Boat.attack()

    
    pygame.display.update()

pygame.quit()