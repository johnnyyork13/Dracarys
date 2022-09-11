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
        self.deltax = 0
        self.deltay = 0
        self.fireball_list = []
        self.dragon_one = pygame.image.load("dragon_one.png")
        self.dragon_two = pygame.image.load("dragon_two.png")
        self.dragon_image_list = [self.dragon_one, self.dragon_two]
        self.dragon_image_count = 0
        self.fire_one = pygame.image.load("fire_one.png")
        

    def movement(self, collision):
        keys = pygame.key.get_pressed()

        self.deltax = 0
        self.deltay = 0

        if keys[pygame.K_d]:
            self.deltax += self.vel
        if keys[pygame.K_a]:
            self.deltax -= self.vel
        if keys[pygame.K_w]:
            self.deltay -= self.vel
        if keys[pygame.K_s]:
            self.deltay += self.vel

        #Check for X AXIS collision
        if not collision[0]:
            self.x += self.deltax
        #Check for Y AXIS collision
        if not collision[1]:
            self.y += self.deltay

    def collision(self):
        x_collide = False
        y_collide = False

        if self.x + self.deltax < 0 or self.x + self.deltax + self.width > self.SCREEN_WIDTH:
            x_collide = True
        else:
            x_collide = False
        if self.y + self.deltay < 0 or self.y + self.deltay + self.height > self.SCREEN_HEIGHT:
            y_collide = True
        else:
            y_collide = False

        return [x_collide, y_collide]

    def attack(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.win.blit(self.fire_one, (self.x+self.width, self.y+30))


    def draw(self):
    
        if self.dragon_image_count <= 10:
            self.win.blit(self.dragon_image_list[0], (self.x, self.y) )
            self.dragon_image_count += 1
        elif self.dragon_image_count <= 20:
            self.win.blit(self.dragon_image_list[1], (self.x, self.y) )
            self.dragon_image_count += 1
        else:
            self.dragon_image_count = 0
        #pygame.draw.rect(self.win, BLUE, (self.x, self.y, self.width, self.height))


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
