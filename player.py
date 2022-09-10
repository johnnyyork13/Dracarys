import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



class Player:

    def __init__(self, win, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.win = win
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.x = 100
        self.y = SCREEN_HEIGHT/2
        self.width = 50
        self.height = 50
        self.vel = 5
        self.x_collide = False
        self.y_collide = False
        self.fireball_list = []
        

    def movement(self, collision):
        keys = pygame.key.get_pressed()

        deltax = 0
        deltay = 0

        #GRAVITY
        deltay += 2

        if keys[pygame.K_d]:
            deltax += self.vel
        if keys[pygame.K_a]:
            deltax -= self.vel
        if keys[pygame.K_w]:
            deltay -= self.vel
        if keys[pygame.K_s]:
            deltay += self.vel

        #Check for X AXIS collision
        if not collision[0]:
            self.x += deltax
        #Check for Y AXIS collision
        if not collision[1]:
            self.y += deltay

    def collision(self):
        x_collide = False
        y_collide = False

        if self.x <= 0 or self.x + self.width >= self.SCREEN_WIDTH:
            x_collide = True
        else:
            x_collide = False
        if self.y <= 0 or self.y + self.height >= self.SCREEN_HEIGHT:
            y_collide = True
        else:
            y_collide = False

        return [x_collide, y_collide]

    def attack(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pygame.draw.rect(self.win, RED, (self.x+self.width, self.y+self.height, self.width, self.height))


    def draw(self):

        pygame.draw.rect(self.win, BLUE, (self.x, self.y, self.width, self.height))


class Boat:

    def __init__(self, win, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.win = win
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.x = SCREEN_WIDTH + 50
        self.y = SCREEN_HEIGHT - 50
        self.width = 50
        self.height = 50
        self.vel = 2

    def movement(self, playerx):
        if self.x >= playerx + self.width*2:
            self.x -= self.vel
        elif self.x < playerx + self.width*2:
            self.x += self.vel

    def attack(self):
        pass

    def draw(self):
        pygame.draw.rect(self.win, GREEN, (self.x, self.y, self.width, self.height))
