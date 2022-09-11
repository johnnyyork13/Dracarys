import pygame
import player
pygame.init()

clock = pygame.time.Clock()

background = pygame.image.load("./sprites/background.png")

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
Boat_Two = player.Boat(win, SCREEN_WIDTH, SCREEN_HEIGHT)

boat_list = []
def make_boats():
    for i in range(1, 5):
        boat = player.Boat(win, SCREEN_WIDTH, SCREEN_HEIGHT)
        boat_list.append(boat)
    
    for boat_id, boat in enumerate(boat_list):
        boat.x = SCREEN_WIDTH + (boat_id * 100)

def player_hit(player_rect, arrow_rect):
    if arrow_rect.colliderect(player_rect):
        return -5
    else:
        return 0

def spawn_boats(boat_list, Drogo):
    for boat in boat_list:
        boat.on_fire = Drogo.attack([boat.x, boat.y, boat.width, boat.height])
        boat.movement(Drogo.x, boat_list)
        boat.draw(boat_list)
        boat.attack(Drogo.x, Drogo.y)
        Drogo.hp_remaining += player_hit(Drogo.player_rect, boat.arrow_rect)

make_boats()


on_fire = False
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

    spawn_boats(boat_list, Drogo)
    #spawn_boats(Boat_Two, Drogo)


    
    pygame.display.update()

pygame.quit()